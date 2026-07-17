from typing import Dict


def count_words(text: str) -> int:
    return len(text.split())


def occurrences(text: str) -> Dict[str, int]:
    characters: Dict[str, int] = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in characters:
            characters[lower_char] = 1
        else:
            characters[lower_char] += 1
    return characters


def sort_on(text: tuple[str, int]) -> int:
    return text[1]


def chars_dict_to_sorted_list(characters: Dict[str, int]) -> list[tuple[str, int]]:
    chars = []
    for character in characters:
        chars.append((character, characters[character]))
    return sorted(chars, reverse=True, key=sort_on)
