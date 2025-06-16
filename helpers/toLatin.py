def to_latin_only(text: str) -> str:
    kirill_to_latin_map = {
        "А": "A", "В": "B", "Е": "E", "К": "K", "М": "M", "Н": "H", "О": "O",
        "Р": "P", "С": "C", "Т": "T", "Х": "X", "а": "a", "е": "e", "о": "o",
        "р": "p", "с": "c", "у": "y", "х": "x"
    }
    return ''.join(kirill_to_latin_map.get(char, char) for char in text)