import numpy as np
from typing import List

def post_processing(pred: np.ndarray) -> List[float]:
    """
    Perform post-processing on the prediction result.

    Args:
        pred (np.ndarray): The prediction result as a NumPy array.

    Returns:
        List[float]: The post-processed prediction result as a list of floats.

    """
    # Convert the prediction array to a list of floats
    postprocessed_prediction = list(map(float, pred))
    
    return postprocessed_prediction
