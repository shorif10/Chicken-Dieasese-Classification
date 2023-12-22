import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

try:
    os.makedirs(log_dir, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format=logging_str,
        handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logger = logging.getLogger("cnnClassifierLogger")
    logger.info("Logging initialized")

except PermissionError as e:
    # PermissionError occurred, log the error
    print(f"Permission Error: {e}. Check if you have write permissions for '{log_dir}' directory.")
    # Log the error to a default location or the console
    logging.basicConfig(level=logging.INFO, format=logging_str)
    logger = logging.getLogger("cnnClassifierLogger")
    logger.error(f"Permission Error: {e}. Check if you have write permissions for '{log_dir}' directory.")
