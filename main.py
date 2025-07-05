from stats import count_words
from stats import count_letters
from stats import dict_sort
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book = (f"{sys.argv[1]}")
    print(f"Analyzing book found at {book}...")
    book_contents = get_book_text(book)
    num_words = count_words(book_contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    letters_list = count_letters(book_contents)
    #print(letters_list)
    sorted = dict_sort(letters_list)
    print("--------- Character Count -------")
    for k,v in sorted.items():
        if k.isalpha() == True:
            print(f"{k}: {v}")
    print("============= END ===============")

main()

 
