import json
from pathlib import Path
import config

MEMORY_FILE = config.MEMORY_FILE


def load_memory():
    """Load memory from JSON file."""
    if not MEMORY_FILE.exists():
        return {
            "user": {},
            "preferences": {},
            "history": []
        }

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(memory):
    """Save memory to JSON file."""
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)