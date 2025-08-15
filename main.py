def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(text: str) -> int:
    return len(text.split())

def main():
    text: str = get_book_text("./books/frankenstein.txt")
    how_many_words: int = count_words(text)
    print(f"{how_many_words} words found in the document")


if __name__ == "__main__":
    main()

