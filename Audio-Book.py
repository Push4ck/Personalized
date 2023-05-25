import pyttsx3  # Importing the pyttsx3 library for text-to-speech conversion
from PyPDF2 import PdfReader  # Importing the PdfReader class from PyPDF2 module
from tkinter import Tk, filedialog  # Importing Tk and filedialog from tkinter module for file browsing

# Open file browser window
root = Tk()
root.withdraw()

# Prompt user to select a PDF file
book_filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

try:
    with open(book_filepath, "rb") as book_file:  # Open the selected PDF file in read-binary mode
        pdf_reader = PdfReader(book_file)  # Create a PdfReader object to read the PDF file
        book_text = ""  # Initialize an empty string to store the extracted text from the PDF

        # Iterate through each page of the PDF and extract the text
        for page in pdf_reader.pages:
            book_text += page.extract_text()

except FileNotFoundError:
    print("File not found. Please make sure the file path is correct.")
    exit()

# Initialize the pyttsx3 engine for text-to-speech conversion
engine = pyttsx3.init()

# Set the speech rate to 300 words per minute
engine.setProperty('rate', 300)

# Convert the extracted text to speech
engine.say(book_text)

# Run the text-to-speech engine and wait for the speech to finish
engine.runAndWait()
