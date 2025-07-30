import typer
from pdf_merger.core import merge_pdfs, remove_original_pdfs
from tkinter import Tk, filedialog
from typing import Optional
import os

app = typer.Typer()

@app.command()
def merge(
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output filename (e.g. merged.pdf)"),
    cleanup: bool = typer.Option(False, "--cleanup", "-c", help="Remove original files after merging"),
):
    """
    Merge selected PDF files into a single file.
    """
    root = Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF Files", "*.pdf")])

    if not file_paths:
        typer.echo("No files selected.")
        raise typer.Exit()

    output_file = output or filedialog.asksaveasfilename(title="Save Merged PDF As", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if not output_file:
        typer.echo("No output file selected.")
        raise typer.Exit()

    try:
        merge_pdfs(file_paths, output_file)
        typer.echo(f"Merged into: {output_file}")
    except Exception as e:
        typer.echo(f"Error during merge: {e}")
        raise typer.Exit()

    if cleanup:
        remove_original_pdfs(file_paths)
        typer.echo("Original files removed.")
