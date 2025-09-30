def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_num_chars(text: str) -> dict[str, int]:
    num_chars: dict[str, int] = {}
    for char in text:
        c = char.lower()
        if c in num_chars:
            num_chars[c] += 1
        else:
            num_chars[c] = 1
    return num_chars
