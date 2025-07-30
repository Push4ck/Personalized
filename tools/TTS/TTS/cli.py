import typer
from tts.core import text_to_speech
from pathlib import Path

app = typer.Typer()

@app.command()
def speak(
    text: str = typer.Option(..., "--text", "-t", help="Text to convert to speech"),
    output: str = typer.Option("output.mp3", "--output", "-o", help="Output file path"),
    lang: str = typer.Option("en", "--lang", "-l", help="Language code (default: en)"),
    slow: bool = typer.Option(False, "--slow", "-s", help="Slow speech mode"),
    play: bool = typer.Option(False, "--play", "-p", help="Play audio after saving")
):
    """Convert text to speech and save to MP3."""
    try:
        output_path = str(Path(output).resolve())
        text_to_speech(text, output_path, lang, slow, play)
        typer.echo(f"Speech saved to: {output_path}")
    except Exception as e:
        typer.echo(f"Error: {e}")
