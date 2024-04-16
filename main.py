from pprint import pprint

def main():
    book_file = "books/frankenstein.txt"
    content = read(book_file)
    print(f"--- Begin report of {book_file} ---")
    for stat in chars_count(content):
        print(f"The character {stat["char"]} was found {stat["count"]} times")
    print(f"--- End report ---")

def sort_on(dict):
    return dict["count"]

def char_dict_to_list(dict):
    characters = list()
    for char,count in dict.items():
        if char.isalpha():
            characters.append({"char": char, "count": count})
    characters.sort(key=sort_on, reverse=True)
    return characters

def chars_count(book):
    char_dict = dict()
    for letter in book.lower():
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1
    return char_dict_to_list(char_dict)

def word_count(book):
    return len(book.split())

def read(path):
    with open(path, "r") as book:
        return book.read()
    
main()