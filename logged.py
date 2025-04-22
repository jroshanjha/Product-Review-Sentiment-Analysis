# logged.py
import logging
from logging.handlers import RotatingFileHandler
import os

def set_logger():
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, 'app.log')

    handler = RotatingFileHandler(log_path, maxBytes=10000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger("flask_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(handler)
        logger.info("✅ Logger initialized successfully.")

    return logger
