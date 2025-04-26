def get_book_text(file_path):
    with open(file_path, 'r') as f:
        file_contents = f.read()
        return file_contents

def number_of_words(book_text):
    split_book_text = book_text.split()
    return len(split_book_text)

def dict_of_letters(book_text):
    book_text = list(book_text.lower())
    my_dict = {}
    for letter in book_text:
        number_of_words = my_dict.get(letter, 0)
        number_of_words += 1
        my_dict.update({letter: number_of_words})
    return my_dict

def sorted_dict(my_dict):
    return sorted(my_dict.items(), key=lambda item: item[1], reverse=True)