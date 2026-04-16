import pytesseract
from PIL import Image
import re
import cv2
import numpy as np

import sys
import os
from pathlib import Path
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
import config

class OCRReader:
    def __init__(self, lang='fin'):
        # Point to the Tesseract binary
        self.lang = lang
        pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH
    def filter_text(self, text):
        """Cleans up the raw OCR output."""
        result = []
        for line in text.split("\n"):
            line = line.strip()
            if not line: continue
            # Remove punctuation and noise
            clean_line = re.sub(r"[—_\.,!?'\"\\']", " ", line)
            # Remove extra spaces
            clean_line = " ".join(clean_line.split())
            if clean_line:
                result.append(clean_line)
        return result

    def read_text(self, name):
        image_path = config.ASSETS_DIR / name
        if not image_path.exists():
            print(f"Error: File not found at {image_path}")
            return []
        img = Image.open(image_path)
        raw_text = pytesseract.image_to_string(img, lang=self.lang,config='--psm 6')
        return self.filter_text(raw_text)


if __name__ == "__main__":
    OCR = OCRReader()
    print(OCR.read_text("test.png"))
