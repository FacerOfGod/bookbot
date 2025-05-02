import os
from src.utils.stats import *


def run_cli_app(file_path: str):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: '{file_path}'")
    try:
        text = get_book_text(file_path)
        num_words = number_of_words(text)
        my_dict = dict_of_letters(text)
        character_frequency_sorted = sorted_dict(my_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("----------- Character Count ----------")
        for character, count in character_frequency_sorted:
            if character.isalpha():
                print(f"{character}: {count}")
        print("============= END ===============")
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")
