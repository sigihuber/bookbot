from stats import get_num_words, get_num_chars, sort_num_chars
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_chars = sort_num_chars(num_chars)
    generate_report(book_path, num_words, sorted_chars)


# Returns the content of a text file as a string
def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


# Generate Report
def generate_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


main()
