import pytest
from tts.core import text_to_speech
import os

def test_empty_text():
    with pytest.raises(ValueError):
        text_to_speech("")

def test_valid_text(tmp_path):
    output_file = tmp_path / "test.mp3"
    text_to_speech("Hello", str(output_file))
    assert output_file.exists()
