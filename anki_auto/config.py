import os
from pathlib import Path

# Get the directory where config.py lives
BASE_DIR = Path(__file__).resolve().parent

# Folders
ASSETS_DIR = BASE_DIR / "assets"
CORE_DIR = BASE_DIR / "core"
UI_DIR = BASE_DIR / "UI"

# Ensure folders exist
ASSETS_DIR.mkdir(exist_ok=True)
CORE_DIR.mkdir(exist_ok=True)
UI_DIR.mkdir(exist_ok=True)

# API Configuration
ANKI_URL = "http://localhost:8765"
ANKI_DECK_NAME = "Finnish Learning"
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Translation Settings
SOURCE_LANG = "fi"
TARGET_LANG = "en"
# Flags
DOUBLE_CHECK = True