import logging
import os

LOG_FOLDER = "Logs"
LOG_FILE = os.path.join(LOG_FOLDER, "jarvis.log")

os.makedirs(LOG_FOLDER, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("Jarvis")