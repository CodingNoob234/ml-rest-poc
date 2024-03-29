import os
import logging

def configure_logger():
    # Map log level names to their corresponding constants
    log_level_mapping = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    # Fetch the log level from environment variables
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    # Set the log level to the corresponding constant from the mapping, or use INFO as the default
    log_level = log_level_mapping.get(log_level, logging.INFO)

    # Configure the logger with the specified log level and other settings
    DEFAULT_LOG_FILE_PATH = "./logs/app.log"
    log_file_path = os.getenv("LOG_FILE_PATH", DEFAULT_LOG_FILE_PATH)
    if log_file_path in ['False', 'false', 'None', 'none']:
        log_file_path = None
    
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=log_file_path,
        filemode='a'
    )