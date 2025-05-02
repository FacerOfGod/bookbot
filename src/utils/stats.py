"""
This module provides functions for analyzing text files, particularly books.
It includes utilities for reading text files, counting words, analyzing letter frequencies,
and sorting the results.

Functions:
    get_book_text: Reads a text file and returns its contents
    number_of_words: Counts the number of words in a text
    dict_of_letters: Creates a frequency dictionary of letters in a text
    sorted_dict: Sorts a dictionary by its values in descending order
"""

import chardet


def get_book_text(file_path: str) -> str:
    """
    Reads and returns the contents of a text file.
    
    Args:
        file_path (str): The path to the text file to be read.
        
    Returns:
        str: The complete contents of the file as a string.
        
    Note:
        The file is read using UTF-8 encoding to handle special characters.
    """
    with open(file_path, "rb") as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result["encoding"]

    with open(file_path, "r", encoding=encoding) as f:
        file_contents = f.read()
    return file_contents

def number_of_words(book_text: str) -> int:
    """
    Counts the number of words in a given text.
    
    Args:
        book_text (str): The text to count words from.
        
    Returns:
        int: The total number of words in the text.
        
    Note:
        Words are split by whitespace characters.
    """
    split_book_text = book_text.split()
    return len(split_book_text)

def dict_of_letters(book_text: str) -> dict:
    """
    Creates a dictionary counting the occurrences of each letter in the text.
    
    Args:
        book_text (str): The text to analyze.
        
    Returns:
        dict: A dictionary where keys are lowercase letters and values are their counts.
        
    Note:
        The text is converted to lowercase before counting, so 'A' and 'a' are counted as the same letter.
    """
    book_text = list(book_text.lower())
    my_dict = {}
    for letter in book_text:
        number_of_words = my_dict.get(letter, 0)
        number_of_words += 1
        if letter.isalpha():        
            my_dict.update({letter: number_of_words})
    return my_dict

def sorted_dict(my_dict: dict) -> list:
    """
    Sorts a dictionary by its values in descending order.
    
    Args:
        my_dict (dict): The dictionary to be sorted.
        
    Returns:
        list: A list of tuples containing (key, value) pairs, sorted by value in descending order.
        
    Example:
        >>> sorted_dict({'a': 2, 'b': 1, 'c': 3})
        [('c', 3), ('a', 2), ('b', 1)]
    """
    return sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

def file_path_to_stats(file_path: str) -> tuple[str, int, dict]:
    """
    Process a text file and extract various statistics about its contents.
    
    This function reads a text file and analyzes it to provide:
    - The complete text content
    - The total number of words
    - A sorted dictionary of character occurrences
    
    Args:
        file_path (str): The path to the text file to analyze
        
    Returns:
        tuple[str, int, dict]: A tuple containing:
            - str: The complete text content of the file
            - int: The total number of words in the file
            - dict: A sorted dictionary where:
                - Keys are characters from the text
                - Values are the number of occurrences of each character
                - The dictionary is sorted by occurrence count in descending order
    
    """
    book_text = get_book_text(file_path)
    total_words = number_of_words(book_text)
    sort_dict = sorted_dict(dict_of_letters(book_text))
    return book_text, total_words, sort_dict