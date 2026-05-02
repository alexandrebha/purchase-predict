import pandas as pd
from purchase_predict.pipelines.loading.nodes import load_csv_from_bucket

def test_node_exists():
    assert callable(load_csv_from_bucket)

import pandas as pd

from purchase_predict.pipelines.loading.nodes import load_csv_from_bucket


def test_load_csv_from_bucket(project_id, primary_folder):
    df = load_csv_from_bucket(project_id, primary_folder)
    print(df.head())