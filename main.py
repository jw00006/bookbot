def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"There are {num_words} words in the book.")
    num_chars = count_characters(text)
    print(f"There are {num_chars} in the book.")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    char_list = {}
    for char in text:
        if char.isalpha() or char == " ":
            if char not in char_list:
                char_list[char] = 0
            char_list[char] += 1
    return char_list


main()