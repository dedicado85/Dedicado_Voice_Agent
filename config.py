from pathlib import Path

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "Data"

MEMORY_FILE = DATA_DIR / "memory.json"

LLM_MODEL = "models/gemini-3.5-flash"