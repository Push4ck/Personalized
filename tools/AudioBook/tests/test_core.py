from audio_book.core import extract_text_from_pdf
import pytest

def test_pdf_extraction_with_invalid_path():
    with pytest.raises(FileNotFoundError):
        extract_text_from_pdf("invalid_path.pdf")
