# 🚀 AnkiCards

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Anki](https://img.shields.io/badge/Anki-Addon-blueviolet)](https://apps.ankiweb.net/)

> A powerful tool for [Anki](https://github.com/ankitects/anki). Automatically import text from images and instantly generate new flashcards for language learning.

---

## 📋 Table of Contents
- [🚀 AnkiCards](#-ankicards)
  - [📋 Table of Contents](#-table-of-contents)
  - [✨ Features](#-features)
  - [🛠 Tech Stack](#-tech-stack)
  - [📂 Project Structure](#-project-structure)
  - [📦 Quick Start](#-quick-start)
    - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [How to use](#how-to-use)

---

## ✨ Features
* **Anki Integration:** Built specifically as a native Anki tool.
* **OCR Processing:** Effortlessly extract text from images using EasyOCR.
* **Smart Automation:** Automatically creates new cards from detected words.
* **Optimization:** High-performance algorithms for fast text recognition and processing.

---

## 🛠 Tech Stack

| Stack | Tools |
| :--- | :--- |
| **Language** | Python 3.12 |
| **OCR Engine** | [Tesseract](https://github.com/tesseract-ocr/tesseract) |
| **Translation** | [Argos Translate](https://github.com/argosopentech/argos-translate) |

---

## 📂 Project Structure

```text
anki_auto/
├── assets/             # Icons and static resources
├── core/               # Business logic
│   ├── __init__.py     # Initialisation of package
│   ├── anki_api.py     # Communication with Anki database
│   ├── ocr_engine.py   # EasyOCR implementation
│   └── translator.py   # Argos Translate logic
├── config.py           # Global settings and constants
├── main.py             # Application entry point
└── .gitignore          # Files to exclude from Git
```
---

## 📦 Quick Start

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pirot1/AnkiCards.git
   cd AnkiCards
   ```

### Prerequisites
* **Anki**: Ensure Anki is installed and running.

* **AnkiConnect**: Install the AnkiConnect add-on *(Code: 2055492159)* and restart Anki.

* **Tesseract OCR**: Install Tesseract OCR on your system and ensure the path is correctly set in your config.py.
* **Double check**: if you don't want this feature you are free to set in your config.py file `DOUBLE_CHECK = False`
### How to use
1. **Start Anki:** Ensure Anki is open and running in the background.

2. **Open Terminal:** Navigate to your project root:

```Bash
cd C:\Users\YourName\Desktop\Projects\AnkiProject\AnkiCards
```
**Prepare Asset:** Place your image file (e.g., finnish_words.png) into the assets/ directory.

3. **Run Script:** Execute the main application:
```Bash
python anki_auto\main.py
```
4. **Enter Filename:** When prompted, type the name of the file (e.g., finnish_words.png) and press Enter.
