import sys
from stats import *

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_file = sys.argv[1]
        text = get_book_text(path_file)
        num_words = number_of_words(text)
        my_dict = dict_of_letters(text)
        character_frequency_sorted = sorted_dict(my_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_file}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("----------- Character Count ----------")
        for character, count in character_frequency_sorted :
            if character.isalpha():
                print(f"{character}: {count}")
        print("============= END ===============")


if __name__ == "__main__":
    main()


