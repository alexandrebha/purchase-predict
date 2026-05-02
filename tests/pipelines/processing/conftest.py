import pytest
from purchase_predict.pipelines.loading.nodes import load_csv_from_bucket


@pytest.fixture(scope="session")
def project_id():
    return "purchase-predict-493617"

@pytest.fixture(scope="session")
def primary_folder():
    return "purchase-predict-sara-123/data-test.csv"

@pytest.fixture(scope="module")
def dataset_not_encoded(project_id, primary_folder):
    return load_csv_from_bucket(project_id, primary_folder)