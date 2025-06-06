import sys
from stats import print_num_words, get_book_text, get_char_frequency, sort_dict


def print_characters(sorted_dict):
    for k, v in sorted_dict.items():
        if k.isalpha():
            print(f"{k}: {v}")


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
