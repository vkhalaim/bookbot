import sys
from stats import get_num_words, get_character_frequency, sorted_by_frequency


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(get_num_words(get_book_text(sys.argv[1])))
    print("--------- Character Count -------")
    sorted_ = sorted_by_frequency(get_character_frequency(get_book_text(sys.argv[1])))
    for key, value in sorted_.items():
        print(f"{key}: {value}")