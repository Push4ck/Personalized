from gtts import gTTS
import os

# Set the text to be spoken
text = "Hello I'm your assistant, How can I assist you?"

# Specify the language and gender (optional)
language = 'en'
gender = 'female'

# Generate the speech using gTTS
tts = gTTS(text=text, lang=language, tld='com', slow=False)

# Save the speech to an audio file
output_path = r"C:\Users\pushk\OneDrive\Desktop\Untitled\output.mp3"
tts.save(output_path)

# Play the audio file (optional)
os.system(f'start {output_path}')
