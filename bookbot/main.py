from stats import count_words, occurrences, chars_dict_to_sorted_list
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, encoding="utf-8-sig") as f:
        return f.read()


def print_report(path: str, word_count: int, sorted_list: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for chars in sorted_list:
        if chars[0].isalpha():
            print(f"{chars[0]}: {chars[1]}")
    print("============= END ===============")


def main() -> None:
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    chars = occurrences(book)
    count = count_words(book)
    chars_sorted = chars_dict_to_sorted_list(chars)
    print_report(book_path, count, chars_sorted)


main()
