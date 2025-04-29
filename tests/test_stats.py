from src.utils.stats import get_book_text, number_of_words, dict_of_letters, sorted_dict

def test_get_book_text(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello World\nThis is a test", encoding="utf8")

    result = get_book_text(str(test_file))
    assert result == "Hello World\nThis is a test"

def test_number_of_words():
    assert number_of_words("Hello World") == 2
    assert number_of_words("Hello   World") == 2
    assert number_of_words(" Hello  World ") == 2
    assert number_of_words("") == 0

def test_dict_of_letters():
    result = dict_of_letters("Hello")
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    result = dict_of_letters("HeLLo")
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    result = dict_of_letters("")
    assert result == {}

def test_sorted_dict():
    test_dict = {'a': 2, 'b': 1, 'c': 3}
    result = sorted_dict(test_dict)
    assert result == [('c', 3), ('a', 2), ('b', 1)]

    result = sorted_dict({})
    assert result == [] 