def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_count_words(text)
    letter_dict = get_count_letters(text)
    print_report(book_path, letter_dict, num_words)

def get_count_words(text):
    words = text.split()
    return len(words)

def get_count_letters(text):
    letters = {}
    for word in text:
        word = word.lower()
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def print_report(book_path, letter_dict, num_words):
    print(f"--- Report of {book_path} ---")
    print(f"There are {num_words} words in this book")
    letter_list = list(letter_dict)
    letter_list.sort()
    for letter in letter_list:
        if letter.isalpha():
            print(f"The \"{letter}\" character was found {letter_dict[letter]} times")
    print("--- End Report ---")



main()

