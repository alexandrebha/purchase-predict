from kedro.runner import SequentialRunner
from purchase_predict.pipelines.loading.pipeline import create_pipeline
import pandas as pd

def test_pipeline(catalog_test):
    runner = SequentialRunner()
    pipeline = create_pipeline()
    result = runner.run(pipeline, catalog_test)

    df = result["primary"].load()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.shape[1] == 16
    assert "purchased" in df.columns