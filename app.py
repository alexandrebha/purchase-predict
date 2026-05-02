import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

REQUIRED_FIELDS = [
    "product_id",
    "brand",
    "price",
    "num_views_session",
    "num_views_product",
    "category",
    "sub_category",
    "hour",
    "minute",
    "weekday",
    "duration",
    "num_prev_sessions",
    "num_prev_product_views",
]


def check_fields(body: dict, fields: list) -> list:
    return [f for f in fields if f not in body]


class Model:
    def __init__(self):
        self.model = None
        self.transform_pipeline = None

    def load(self):
        data = joblib.load("data/06_model/model.pkl")
        self.model = data["model"]
        self.transform_pipeline = joblib.load("data/04_feature/transform_pipeline.pkl")

    def predict(self, df: pd.DataFrame) -> list:
        for col, encoder in self.transform_pipeline.items():
            df[col] = df[col].astype("string").fillna("unknown")
            df[col] = encoder.transform(df[col])
        return self.model.predict(df).tolist()


model = Model()
model.load()


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def predict():
    body = request.get_json()
    missing = check_fields(body, REQUIRED_FIELDS)
    if missing:
        return jsonify({"error": f"Champs manquants : {missing}"}), 400

    df = pd.DataFrame([body])
    try:
        predictions = model.predict(df)
        return jsonify({"prediction": predictions[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
