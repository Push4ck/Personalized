import typer
from audio_book.core import extract_text_from_pdf, text_to_speech
from tkinter import Tk, filedialog

app = typer.Typer()

@app.command()
def read(rate: int = 300):
    """
    Convert a selected PDF to speech.
    """
    root = Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    
    if not filepath:
        typer.echo("No file selected.")
        raise typer.Exit()

    try:
        text = extract_text_from_pdf(filepath)
        typer.echo("Reading PDF content aloud...")
        text_to_speech(text, rate=rate)
    except Exception as e:
        typer.echo(f"Error: {e}")

if __name__ == "__main__":
    app()
