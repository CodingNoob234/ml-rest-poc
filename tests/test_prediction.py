import logging
logger = logging.getLogger(__name__)

import pytest
from fastapi.testclient import TestClient
from tests.data.test_messages import payload_succes, payload_fail
import os
import json
from app.main import app

# Create a test client using the FastAPI app
client = TestClient(app)

# Fetch the API endpoint from environment variables
ENDPOINT = os.getenv("API_ENDPOINT", "")

def test_correct_input():
    """
    Test a successful prediction request with correct input data.
    """

    logger.debug("succes input:\n" + str(payload_succes))

    # Send a POST request to the API endpoint
    response = client.post("/api" + ENDPOINT, json=payload_succes)

    # Check the response status code and content
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_wrong_input():
    """
    Test an invalid input request.
    """
    logger.debug("fail input:\n" + str(payload_fail))

    # Send a POST request to the API endpoint
    response = client.post("/api" + ENDPOINT, json=payload_fail)

    # Check the response status code
    assert response.status_code == 400  # Unprocessable Entity


# Run the test module if executed directly
if __name__ == "__main__":
    pytest.main()
