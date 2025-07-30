import pyttsx3
from PyPDF2 import PdfReader
import os

def extract_text_from_pdf(filepath: str) -> str:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, "rb") as file:
        reader = PdfReader(file)
        return "".join(page.extract_text() or "" for page in reader.pages)

def text_to_speech(text: str, rate: int = 300) -> None:
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()
