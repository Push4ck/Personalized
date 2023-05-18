from gtts import gTTS
import os

# Ask the user to input the text
text = input("Please enter the text to be spoken: ")

# Specify the language and gender (optional)
language = 'en'
gender = 'female'

# Generate the speech using gTTS
tts = gTTS(text=text, lang=language, slow=False)

# Specify the path to save the output file
output_path = r"C:\Users\pushk\OneDrive\Desktop\Untitled\output.mp3"

# Save the speech to an audio file
tts.save(output_path)

# Play the audio file (optional)
os.system(f'start {output_path}')
