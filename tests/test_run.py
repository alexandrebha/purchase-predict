import pandas as pd
from purchase_predict.pipelines.loading.nodes import load_csv_from_bucket


def test_load_csv_from_bucket(project_id, primary_folder):
    df = load_csv_from_bucket(project_id, primary_folder)

    # Vérifier que c'est bien un DataFrame
    assert isinstance(df, pd.DataFrame)

    # Vérifier qu'il n'est pas vide
    assert not df.empty

    # Vérifier le nombre de colonnes attendu
    assert df.shape[1] == 16

    # Vérifier une colonne importante
    assert "purchased" in df.columns