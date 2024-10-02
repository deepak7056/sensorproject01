# import logging
# import os
# from datetime import datetime


# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%s')}.log"

# logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)

# os.makedirs(logs_path, exist_ok=True)

# LOG_FILE_PATH= os.path.join(logs_path, LOG_FILE)

# logging.basicConfig(
#     filename= LOG_FILE_PATH,
#     format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level= logging.INFO
# )
import logging
from datetime import datetime
import os

# Correct log file format
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M')}_{int(datetime.now().timestamp())}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Ensure the logs directory exists
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Set up logging configuration
logging.basicConfig(
    filename=logs_path,
    filemode="w",
    format='[%(asctime)s] %(levelname)s: %(message)s',
    level=logging.INFO
)

# Example log message to verify logging works
logging.info("Logging setup successfully.")
