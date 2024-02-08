import logging
logger = logging.getLogger(__name__)

from numpy import asarray
from utils.load_model import model, pre_computed_features

from data_loading.enrich_data import enrich_data
from data_processing.data_validation import validate_json
from data_processing.create_features import create_features
from data_processing.pre_processing import pre_processing
from data_processing.post_processing import post_processing

def make_prediction(input_data):
    """
    Make a prediction based on the provided input data.

    Args:
        input_data: The input data for the prediction.

    Returns:
        The post-processed prediction result.
    """
    
    # Enrich data
    input_data = enrich_data(input_data)
    
    # Validate input
    logger.debug("Input data:\n" + str(input_data))
    validate_json(input_data)
    
    # Pre-process the input data
    preprocessed_data = pre_processing(input_data)

    # Create features using the pre-processed data and pre-computed features
    features = create_features(preprocessed_data, pre_computed_features)

    # Perform prediction using the model
    prediction = model.predict(features)
    logger.debug("Prediction:\n" + str(prediction))

    # Post-process the prediction
    postprocessed_prediction = post_processing(prediction)
    logger.debug("Prediction post-processed:\n" + str(postprocessed_prediction))

    # Return the post-processed prediction
    return postprocessed_prediction
