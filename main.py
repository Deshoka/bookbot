import os

def main():
    book_path = "books/frankenstein"
    book_name = os.path.basename(book_path)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    #print(text)
    #print(num_words)
    #print(num_letters)
    print(f"--- Begin report of the book {book_name} ---")
    print(f"The book contains {num_words} words")
    report(num_letters)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    letter_dict = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in letter_dict:
            letter_dict[lowered] += 1
        else:
            letter_dict[lowered] = 1
    
    return letter_dict

def report(char_dict):
    sorted_char_dict = sorted(char_dict.items(), key=lambda item:item[1], reverse=True)
    for char, num in sorted_char_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {num} times")

main()