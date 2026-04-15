from core.ocr_engine import OCRReader
from core.anki_api import AnkiAPI
from core.translator import fin_en_translator
import config
def process_and_add_to_anki(image_name):
    # 1. Initialize
    reader = OCRReader(lang='fin')
    anki = AnkiAPI()
    # 2. Extract
    print(f"Reading {image_name}...")
    raw_text = reader.read_text(image_name)
    # 3. Translate and add
    dbl = config.DOUBLE_CHECK

    def add_word(txt):
        translated = fin_en_translator(txt)
        try:
            anki.add_note("Default", "Basic", txt, translated)
            print(f"Successfully added: {txt}")
        except Exception as e:
            if "duplicate" in str(e).lower():
                print(f"Skipping: '{txt}' (already exists in Anki)")
            else:
                print(f"Error adding '{txt}': {e}")

    for txt in raw_text:
        if dbl:
            if input(f"Does this word exist - \"{txt}\"? Y/N\n").lower() == "y":
                add_word(txt)
            else:
                continue
        else:
            add_word(txt) 

if __name__ == "__main__":
    name = input("Input your namefile:\n")
    process_and_add_to_anki(name)