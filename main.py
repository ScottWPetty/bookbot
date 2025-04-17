import sys
from stats import get_num_words
from stats import get_num_chars
from stats import get_count_list

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        f.close()
    return contents

def main():
    # check for file path to book
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    chars_dict = get_num_chars(book_text)
    count_list = get_count_list(chars_dict)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for count in count_list:
        if count["character"].isalpha():
            print(f"{count["character"]}: {count["count"]}")
    print(f"============= END ===============")
main()