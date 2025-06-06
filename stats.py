def get_char_frequency(file_contents):
    text = file_contents.lower()
    char_freq = {}
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq


def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    print(f"Found {num_words} total words")


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def sort_on(dict_items):
    return dict_items[1]


def sort_dict(freq_dict):
    sorted_dict = dict(sorted(freq_dict.items(), key=sort_on, reverse=True))
    return sorted_dict
