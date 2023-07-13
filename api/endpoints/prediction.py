import logging
logger = logging.getLogger(__name__)

import os
from fastapi import APIRouter, HTTPException
from jsonschema.exceptions import ValidationError

# Importing necessary modules
from models.ml_model import make_prediction
from models.validation import validate_message
from exceptions.validation import InvalidInputDataError
from exceptions.prediction import PredictionError

# Constants for API endpoint configuration
API_ENDPOINT_PROP = "API_ENDPOINT"
API_ENDPOINT_DEFAULT = "/prediction"

# Fetching the API endpoint from environment variables, or using the default value if not set
endpoint = os.getenv(API_ENDPOINT_PROP, API_ENDPOINT_DEFAULT)

# Creating the API router
router = APIRouter()

@router.post(endpoint)
async def post_make_prediction(message: dict):
    """
    Make a prediction based on the provided message.

    Args:
        message (dict): A dictionary containing the input data for the prediction.

    Returns:
        dict: A dictionary containing the prediction result.

    Raises:
        HTTPException: If there is an error with the input data or during the prediction process.
    """
    try:
        # Logging message received
        logger.info("Message received")
        logger.debug("Message:\n" + str(message))
        
        
        
        # Validating the message
        validate_message(message)

        # Extracting input data from the message and make prediction
        a = message.get("input_data",{})
        p = make_prediction(a)
        logger.debug("Result from make_prediction:\n" + str(p))
        
        # Construct response
        response = {"prediction": p}
        
        # Logging success response
        logger.info("Success response sent")
        logger.debug("Response send:\n" + str(response))
        
        # Returning the prediction result
        return response
    
    # Handling specific exceptions and raising appropriate HTTP exceptions with error details
    except InvalidInputDataError as e:
        logger.error("Invalid message: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid message")
    except PredictionError as e:
        logger.error("Error occurred during prediction: " + str(e))
        raise HTTPException(status_code=500, detail="Prediction error")
    except ValidationError as e:
        logger.error("Invalid input_data: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid input data")
    
    # Catching any unexpected exceptions and raising a generic HTTP exception with error details
    except Exception as e:
        logger.error("An unexpected error occurred: " + str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")
    