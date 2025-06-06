def get_char_frequency(file_contents):
    text = file_contents.lower()
    char_freq = {}
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    print(char_freq)


def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
