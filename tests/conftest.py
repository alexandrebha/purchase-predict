import pytest
from kedro.io import DataCatalog, MemoryDataset

@pytest.fixture(scope="session")
def project_id():
    return "purchase-predict-493617"

@pytest.fixture(scope="session")
def primary_folder():
    return "purchase-predict-sara-123/data-test.csv"

@pytest.fixture(scope="session")
def catalog_test(project_id, primary_folder):
    return DataCatalog(
        {
            "params:gcp_project_id": MemoryDataset(project_id),
            "params:gcs_primary_folder": MemoryDataset(primary_folder),
        }
    )