def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def number_of_words(book_output):
    num_words = len(book_output.split())
    return num_words


def number_per_character(book_output):
    lowercase_text = book_output.lower()
    char_counts = {}

    for char in lowercase_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def sort_on(d):
    return d["num"]


def sort_char_dictionary(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


def main():
    filepath = "books/frankenstein.txt"
    book_output = get_book_text(filepath)
    book_number_words = number_of_words(book_output)
    num_characters = number_per_character(book_output)
    character_sort = sort_char_dictionary(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count -----------")
    print(f"Found {book_number_words} total words")
    print("--------- Character Count ---------")
    print(character_sort)
    for item in character_sort:
        if item["char"].isalpha():
            print(f"{item['char']:, } {item['num']}")
    print("=========== END ===========")


main()
