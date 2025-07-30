from gtts import gTTS
import os

def text_to_speech(text: str, output_path: str = "output.mp3", lang: str = "en", slow: bool = False, play: bool = False):
    if not text.strip():
        raise ValueError("Text input cannot be empty.")

    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(output_path)

    if play:
        try:
            os.startfile(output_path)  # Windows only
        except AttributeError:
            os.system(f'xdg-open "{output_path}"')  # Linux
        except Exception as e:
            print(f"Error playing file: {e}")
