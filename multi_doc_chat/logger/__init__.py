import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate log file name based on current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Provide a standard logger instance
logger = logging.getLogger("multi_doc_chat")

# For structured logging compatibility used in some files
class StructLogger:
    def __init__(self, name="multi_doc_chat"):
        self.logger = logging.getLogger(name)
    
    def info(self, msg, **kwargs):
        self.logger.info(f"{msg} | {kwargs}")
        
    def error(self, msg, **kwargs):
        self.logger.error(f"{msg} | {kwargs}")
        
    def warning(self, msg, **kwargs):
        self.logger.warning(f"{msg} | {kwargs}")

log = StructLogger()
