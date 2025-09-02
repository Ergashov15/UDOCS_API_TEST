import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Configure file handler to write logs to a file
file_handler = logging.FileHandler('logs/api.log')
file_handler.setLevel(logging.DEBUG)

# Formatter for the logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add only the file handler to the logger
logger.addHandler(file_handler)


# logs papkasini yaratish (agar mavjud bo'lmasa)
os.makedirs('logs', exist_ok=True)

file_handler = logging.FileHandler('logs/api.log')
# continue setting up logger...
