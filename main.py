import sys

from stats import number_of_words, number_per_character, sort_char_dictionary, sort_on


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_output = get_book_text(filepath)
    book_number_words = number_of_words(book_output)
    num_characters = number_per_character(book_output)
    character_sort = sort_char_dictionary(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count -----------")
    print(f"Found {book_number_words} total words")
    print("--------- Character Count ---------")
    for item in character_sort:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("=========== END ===========")


main()
