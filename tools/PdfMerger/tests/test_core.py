from pdf_merger.core import merge_pdfs
import os

def test_merge_creates_file(tmp_path):
    pdf1 = tmp_path / "file1.pdf"
    pdf2 = tmp_path / "file2.pdf"
    output = tmp_path / "output.pdf"

    # Create dummy PDFs
    pdf1.write_bytes(b"%PDF-1.4\n%...")
    pdf2.write_bytes(b"%PDF-1.4\n%...")

    merge_pdfs([str(pdf1), str(pdf2)], str(output))
    assert output.exists()
