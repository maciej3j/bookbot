import sys

from stats import count_words, count_each_character, sort_dict


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text: str = get_book_text(path)
    how_many_words: int = count_words(text)
    # print(f"{how_many_words} words found in the document")
    # print(f"{count_each_character(text)}")
    print(
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {path}\n"
        "----------- Word Count ----------\n"
        f"Found {how_many_words} total words\n"
        "--------- Character Count -------"
    )
    every_character: list = sort_dict(count_each_character(text))
    for ch in every_character:
        print(f"{ch['name']}: {ch['num']}")


if __name__ == "__main__":
    main()
