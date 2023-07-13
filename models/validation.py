import logging
logger = logging.getLogger(__name__)
from exceptions.validation import InvalidInputDataError
from collections.abc import Sequence

def validate_message(message: dict):
    if not isinstance(message, dict):
        raise InvalidInputDataError("message", "Invalid message format. Expected a dictionary.")

    if "input_data" not in message.keys():
        raise InvalidInputDataError("message", "'input_data' is not a key in dictionary")