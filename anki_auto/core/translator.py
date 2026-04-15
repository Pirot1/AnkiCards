import argostranslate.package
import argostranslate.translate

import sys
import os
from pathlib import Path
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
import config

from_code = config.SOURCE_LANG
to_code = config.TARGET_LANG

# Download and install Argos Translate package
def fin_en_translator(text: str) -> str:
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    available_package = list(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )[0]
    download_path = available_package.download()
    argostranslate.package.install_from_path(download_path)

    # Translate
    installed_languages = argostranslate.translate.get_installed_languages()
    from_lang = list(filter(
            lambda x: x.code == from_code,
            installed_languages))[0]
    to_lang = list(filter(
            lambda x: x.code == to_code,
            installed_languages))[0]
    translation = from_lang.get_translation(to_lang)
    translatedText = translation.translate(text)
    return translatedText

if __name__ == "__main__":
    words = ["Äiti","emä","rakkaus"]
    for word in words:
        print(f"{word} : {fin_en_translator(word)}")
        
