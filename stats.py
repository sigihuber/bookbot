# Returns the number of words in the text.
def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


# Returns the number of characters in the text.
def get_num_chars(text: str) -> dict[str, int]:
    num_chars: dict[str, int] = {}
    for char in text:
        c = char.lower()
        if c in num_chars:
            num_chars[c] += 1
        else:
            num_chars[c] = 1
    return num_chars


# The function takes a dictionary and returns the value of the "num" key.
# This is how the `.sort()` method knows how to sort the list of dictionaries.
def sort_on(items):
    return items["num"]


# Takes a dictionary of character counts and returns a sorted list of dictionaries.
def sort_num_chars(num_chars):
    char_list = []
    for char in num_chars:
        char_list.append({"char": char, "num": num_chars[char]})
    char_list.sort(key=sort_on, reverse=True)
    return char_list
