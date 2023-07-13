# Load environment variables from the appropriate .env file
import logging
logger = logging.getLogger(__name__)

import os
import ssl

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

ssl_context = {
    "ssl_keyfile": ssl_keyfile if ssl_enabled else None,
    "ssl_keyfile_password": ssl_keyfile_password if ssl_enabled else None,
    "ssl_certfile": ssl_certfile if ssl_enabled else None,
}