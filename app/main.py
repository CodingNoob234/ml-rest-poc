# Load environment variables from the appropriate .env file
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'properties.env')
load_dotenv(dotenv_path)

import logging
import ssl
# from ssl import PROTOCOL_TLSv1_2
from fastapi import FastAPI
from api.endpoints.prediction import router as prediction_router
from api.endpoints.health import router as health_router
from utils.configure_logger import configure_logger
from utils.configure_ssl import ssl_context

# Configure and get logger
configure_logger()
logger = logging.getLogger(__name__)

# Initialise the API
app = FastAPI()

# Mount the prediction router
app.include_router(prediction_router, prefix="/api")

# Mount the health router for liveliness/readiness
app.include_router(health_router, prefix="/health")

# Verify SSL Version
logger.info("Configuring SSL for version %s" % (ssl.OPENSSL_VERSION))

# SSL configuration
ssl_keyfile_password = os.getenv("SSL_KEYFILE_PASSWORD")
ssl_keyfile = os.getenv("SSL_KEYFILE")
ssl_certfile = os.getenv("SSL_CERTFILE")

# Check if SSL enabled
ssl_enabled = False
if ssl_keyfile and ssl_keyfile_password and ssl_certfile:
    ssl_enabled = False if os.getenv("SSL_ENABLED") in ["False", "false"] else True

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, 
        host="0.0.0.0", 
        port=8000, 
        **ssl_context
    )