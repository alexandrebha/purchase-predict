# n'oubliez pas d'inclure : import pandas as pd
from purchase_predict.pipelines.processing.nodes import encode_features

def test_encode_features(dataset_not_encoded):
    df = encode_features(dataset_not_encoded)["features"]
    print(df.head())