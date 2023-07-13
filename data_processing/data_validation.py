import logging
logger = logging.getLogger(__name__)

from jsonschema import validate
from data_processing.input_schema import input_schema

def validate_json(json_data):
    validate(instance=json_data, schema=input_schema)