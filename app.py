import os
import uuid
import joblib
import pandas as pd
import numpy as np

from flask import Flask, request, render_template, redirect, url_for, flash, jsonify

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor,
    GradientBoostingClassifier,
    GradientBoostingRegressor
)

from sklearn.linear_model import (
    LogisticRegression,
    LinearRegression,
    Ridge
)

from sklearn.tree import (
    DecisionTreeClassifier,
    DecisionTreeRegressor
)

from sklearn.svm import (
    SVC,
    SVR
)

from sklearn.neighbors import (
    KNeighborsClassifier,
    KNeighborsRegressor
)

from sklearn.metrics import accuracy_score, r2_score


# -----------------------------------
# Flask
# -----------------------------------
app = Flask(__name__)
app.secret_key = "secret"

os.makedirs("models", exist_ok=True)
os.makedirs("uploads", exist_ok=True)

MODEL_PATH = "models/best_model.pkl"


# -----------------------------------
# Detect target column
# -----------------------------------
def detect_target(df):

    targets = [
        "target",
        "label",
        "output",
        "class",
        "salary",
        "price",
        "churn"
    ]

    for col in df.columns:
        if col.lower() in targets:
            return col

    return df.columns[-1]


# -----------------------------------
# Detect ML task
# -----------------------------------
def detect_task(y):

    if y.dtype == "object":
        return "classification"

    if pd.api.types.is_numeric_dtype(y):

        if y.nunique() <= 8:
            return "classification"

        return "regression"

    return "classification"


# -----------------------------------
# Home
# -----------------------------------
@app.route("/")
def index():
    return render_template("index.html")


# -----------------------------------
# Train
# -----------------------------------
@app.route("/train", methods=["POST"])
def train():

    file = request.files.get("file")

    if not file:
        flash("Upload CSV", "danger")
        return redirect("/")

    path = os.path.join(
        "uploads",
        f"{uuid.uuid4().hex}.csv"
    )

    file.save(path)

    df = pd.read_csv(path)

    target = detect_target(df)

    X = df.drop(columns=[target])
    y = df[target]

    # missing values

    for col in X.select_dtypes(include=[np.number]).columns:

        X[col] = X[col].fillna(
            X[col].median()
        )

    for col in X.select_dtypes(
            include=["object", "category"]
    ).columns:

        X[col] = X[col].fillna(
            X[col].mode()[0]
        )

    # detect task

    task = detect_task(y)

    num_cols = X.select_dtypes(
        include=[np.number]
    ).columns.tolist()

    cat_cols = X.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    preprocessor = ColumnTransformer([
        (
            "num",
            StandardScaler(),
            num_cols
        ),
        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            cat_cols
        )
    ])

    # models

    if task == "classification":

        models = {
            "RandomForest":
                RandomForestClassifier(),

            "Logistic":
                LogisticRegression(
                    max_iter=1000
                ),

            "SVM":
                SVC(),

            "DecisionTree":
                DecisionTreeClassifier(),

            "KNN":
                KNeighborsClassifier(),

            "GradientBoosting":
                GradientBoostingClassifier()
        }

        metric = accuracy_score

    else:

        models = {

            "RandomForest":
                RandomForestRegressor(),

            "Linear":
                LinearRegression(),

            "Ridge":
                Ridge(),

            "DecisionTree":
                DecisionTreeRegressor(),

            "KNN":
                KNeighborsRegressor(),

            "GradientBoosting":
                GradientBoostingRegressor(),

            "SVR":
                SVR()
        }

        metric = r2_score

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    best_score = -999
    best_model = None
    best_name = None

    for name, model in models.items():

        try:

            pipe = Pipeline([
                (
                    "prep",
                    preprocessor
                ),
                (
                    "model",
                    model
                )
            ])

            pipe.fit(
                X_train,
                y_train
            )

            preds = pipe.predict(
                X_test
            )

            score = metric(
                y_test,
                preds
            )

            if score > best_score:

                best_score = score
                best_model = pipe
                best_name = name

        except:
            continue

    joblib.dump({

        "model": best_model,

        "task": task,

        "target": target,

        "columns":
            X.columns.tolist()

    }, MODEL_PATH)

    return render_template(
        "result.html",

        training=True,

        task=task,

        best_model=best_name,

        score=round(
            best_score,
            4
        ),

        target=target
    )


# -----------------------------------
# Test
# -----------------------------------
@app.route("/test", methods=["POST"])
def test():

    if not os.path.exists(MODEL_PATH):

        flash(
            "Train first",
            "danger"
        )

        return redirect("/")

    file = request.files.get("file")

    if not file:
        return redirect("/")

    df = pd.read_csv(file)

    model_data = joblib.load(
        MODEL_PATH
    )

    pipe = model_data["model"]

    target = model_data["target"]

    task = model_data["task"]

    X = df.drop(
        columns=[target]
    )

    y = df[target]

    pred = pipe.predict(X)

    if task == "classification":

        score = accuracy_score(
            y,
            pred
        )

        metric = "Accuracy"

    else:

        score = r2_score(
            y,
            pred
        )

        metric = "R²"

    return render_template(
        "result.html",

        testing=True,

        test_score=round(
            score,
            4
        ),

        metric_name=metric
    )


# -----------------------------------
# Predict
# -----------------------------------
@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    text = request.form.get(
        "inputdata"
    )

    model = joblib.load(
        MODEL_PATH
    )

    pipe = model["model"]

    cols = model["columns"]

    data = {}

    for line in text.split("\n"):

        if "=" in line:

            k, v = line.split("=")

            try:
                v = float(v)

            except:
                pass

            data[k.strip()] = v

    X = pd.DataFrame([data])

    for col in cols:

        if col not in X:

            X[col] = 0

    pred = pipe.predict(X)[0]

    return render_template(
        "result.html",

        predicting=True,

        prediction=str(pred)
    )


# -----------------------------------
# API
# -----------------------------------
@app.route(
    "/predict_json",
    methods=["POST"]
)
def predict_json():

    model = joblib.load(
        MODEL_PATH
    )

    pipe = model["model"]

    data = request.json

    pred = pipe.predict(
        pd.DataFrame([data])
    )[0]

    return jsonify({
        "prediction":
            str(pred)
    })


if __name__ == "__main__":
    app.run(
        debug=True
    )
