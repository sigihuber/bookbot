from stats import get_num_words, get_num_chars, sort_num_chars


def main():
    book_path = "books/frankenstein.txt"
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
    print(f"Analyzing book fond at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


main()
