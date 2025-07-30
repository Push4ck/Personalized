from PyPDF4 import PdfFileMerger
import os

def merge_pdfs(file_paths: list[str], output_file: str) -> None:
    merger = PdfFileMerger()
    for file_path in file_paths:
        merger.append(file_path)
    merger.write(output_file)
    merger.close()

def remove_original_pdfs(file_paths: list[str]) -> None:
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
