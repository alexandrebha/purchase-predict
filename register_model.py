import mlflow
import mlflow.sklearn
import joblib

mlflow.set_tracking_uri("http://34.14.93.96:5000")

model = joblib.load("data/06_model/model.pkl")

with mlflow.start_run():
    mlflow.lightgbm.log_model(
        lgb_model=model,
        artifact_path="model",
        registered_model_name="purchase_predict",
    )
    mlflow.log_artifact("data/04_feature/transform_pipeline.pkl")

client = mlflow.MlflowClient()
versions = client.search_model_versions("name='purchase_predict'")
latest = versions[-1].version
client.set_registered_model_alias("purchase_predict", "production", latest)

print(f"Modèle version {latest} enregistré avec alias 'production'")
