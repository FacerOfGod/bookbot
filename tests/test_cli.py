
import pytest
from src.cli.cli_app import run_cli_app
from src.utils.stats import get_book_text, number_of_words, dict_of_letters, sorted_dict

@pytest.fixture
def sample_text_file(tmp_path):
    """Create a temporary text file with known content for testing."""
    content = """This is a test file. It contains some text for testing purposes. The quick brown fox jumps over the lazy dog."""
    file_path = tmp_path / "test.txt"
    file_path.write_text(content)
    return str(file_path)

@pytest.fixture
def empty_text_file(tmp_path):
    """Create an empty text file for testing."""
    file_path = tmp_path / "empty.txt"
    file_path.write_text("")
    return str(file_path)

def test_cli_with_valid_file(sample_text_file, capsys):
    """Test CLI with a valid text file."""
    run_cli_app(sample_text_file)
    
    captured = capsys.readouterr()
    output = captured.out
    
    assert "============ BOOKBOT ============" in output
    assert f"Analyzing book found at {sample_text_file}..." in output
    assert "----------- Word Count ----------" in output
    assert "----------- Character Count ----------" in output
    assert "============= END ===============" in output
    
    text = get_book_text(sample_text_file)
    expected_words = number_of_words(text)
    assert f"Found {expected_words} total words" in output
    
    char_dict = dict_of_letters(text)
    sorted_chars = sorted_dict(char_dict)
    for char, count in sorted_chars:
        if char.isalpha():
            assert f"{char}: {count}" in output

def test_cli_with_empty_file(empty_text_file, capsys):
    """Test CLI with an empty text file."""
    run_cli_app(empty_text_file)
    
    captured = capsys.readouterr()
    output = captured.out
    assert "Found 0 total words" in output

def test_cli_with_missing_file():
    """Test CLI with a non-existent file."""
    non_existent_file = "non_existent.txt"
    
    with pytest.raises(FileNotFoundError):
        run_cli_app(non_existent_file)

def test_cli_with_invalid_encoding(tmp_path, capsys):
    """Test CLI with a file containing invalid encoding."""
    file_path = tmp_path / "invalid.txt"
    with open(file_path, 'wb') as f:
        f.write(b'\x80invalid')
    
    run_cli_app(str(file_path))
    
    captured = capsys.readouterr()
    output = captured.out
    assert "============ BOOKBOT ============" in output
