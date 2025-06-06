import sys
from stats import get_book_text, print_num_words
from stats import get_char_frequency, sort_dict, print_characters


if __name__ == "__main__":

    print("============ BOOKBOT ============")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_content = get_book_text(book)
    print(f"Analyzing book found at {book}...")

    print("----------- Word Count ----------")
    print_num_words(book_content)

    print("--------- Character Count -------")
    sorted_dict = sort_dict(get_char_frequency(book_content))
    print_characters(sorted_dict)
    print("============= END ===============")
