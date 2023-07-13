import pandas as pd
from typing import Dict

required_columns = ["Amount"] + [f"V{i}" for i in range(1, 29)]

def pre_processing(input_data: Dict[str, list]) -> pd.DataFrame:
    """
    Perform pre-processing on the input data dictionary.

    Args:
        input_data (Dict[str, list]): The input data dictionary.

    Returns:
        pd.DataFrame: The pre-processed input data as a pandas DataFrame.

    Raises:
        ValueError: If any of the required columns is missing in the input data.

    """
    # Check if all required columns are present in the input data dictionary
    for c in required_columns:
        if c not in input_data.keys():
            raise ValueError(f"'{c}' must be present in the input data")

    try:
        # Convert the input data dictionary to a pandas DataFrame
        input_data = pd.DataFrame(input_data)[required_columns]
        return input_data
    except:
        raise ValueError("Failed to convert input data to DataFrame.")
