import os 
import logging
import sys

# Define the format of the logs
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Set the directory and log file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")

# ✅ FIX: Use os.makedirs instead of os.mkdirs
os.makedirs(log_dir, exist_ok=True)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),     # Log to file
        logging.StreamHandler(sys.stdout)      # Also show logs in console
    ]
)

# ✅ FIX: getlogger → getLogger (capital G)
logger = logging.getLogger("datascienceproject")
