from pathlib import Path

# -----------------------
# Project Information
# -----------------------

APP_NAME = "Jarvis"
VERSION = "1.0.0"

# -----------------------
# Paths
# -----------------------

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "Data"
LOG_DIR = BASE_DIR / "Logs"
MODELS_DIR = BASE_DIR / "Models"

# -----------------------
# Voice
# -----------------------

VOICE_NAME = "en-US-AndrewNeural"

# -----------------------
# Wake Word
# -----------------------

WAKE_WORD = "hey jarvis"

# -----------------------
# Memory
# -----------------------

MEMORY_FILE = DATA_DIR / "memory.json"
LOG_FILE = LOG_DIR / "jarvis.log"