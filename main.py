def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print(f"--- Begin report of {book_path} ---")

    num_words = count_words(text)
    print(f"There are {num_words} words in the book.")
    
    num_chars = count_characters(text)  
    sorted_chars = sorted_report(num_chars)
    for item in sorted_chars:
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")
    

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
        if char.isalpha():
            if char not in char_list:
                char_list[char] = 0
            char_list[char] += 1
    return char_list

def sorted_report(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    def count_extractor(item):
        return item["count"]
    
    char_list.sort(key=count_extractor, reverse=True)
    return char_list


main()