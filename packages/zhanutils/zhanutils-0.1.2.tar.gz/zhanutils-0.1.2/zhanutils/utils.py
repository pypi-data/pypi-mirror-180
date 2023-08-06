from typing import Dict
import json
import pandas

def get_secret(secret_json_file: str ) -> Dict:
    """
    get secrets
    Args:
        secret_json_file: a json containing secrets

    Returns: a dictionary containing secrets

    """
    with open(secret_json_file) as myfile:
        return json.load(myfile)

def max_pandas_display(pd: pandas, max_row: int = 100) -> None:
    """
    set pandas print format to print all
    Args:
        pd: pandas object

    Returns: None

    """
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", max_row)
    pd.set_option("display.width", None)
    pd.set_option("display.max_colwidth", None)
    pd.set_option("display.expand_frame_repr", False)
