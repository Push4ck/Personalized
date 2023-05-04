import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Select the Microsoft Zira voice
for voice in voices:
    if voice.name == 'Microsoft Zira Desktop':
        engine.setProperty('voice', voice.id)
        break

# Set the rate and volume of the speech
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

# Set the text to be spoken
text = "Baby!!! muu m lelo naaa please!"

# Specify the path to save the output file
output_path = r"C:\Users\pushk\OneDrive\Desktop\Untitled\output.mp3"

# Convert the text to speech and save to file
engine.save_to_file(text, output_path)
engine.runAndWait()
