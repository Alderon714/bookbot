#
# main.py
# 
# Daniel S Cochran
# September 25, 2024 creation date
# 

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) # huge string
    # print(text) # print string : removed book printout
    total_word_count = word_count(book_path) # count words and letters used in file/path
    letters_dict = letter_count(book_path)
    produce_report(book_path,letters_dict,total_word_count)
    
def get_book_text(path):
    # This will take a path/to/file and return a read of the file's content.
    with open(path) as f:
        return f.read()

def word_count(file_path):
    # This will input a text file as a string and print the word count. 
    #
    # The second part counts each letter and provides a count of times used in the file.
    #
    with open(file_path, 'r') as file: 
        text = file.read() 
        words = text.split() 
        count = len(words)
    return count # Added return of count of words as integer
        # print(" *** word count ***")
        # print(f"The text file contains {count} words.")

def letter_count(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        # Now get the number of times the letter is used in the book (text file)
        char_counts = char_count(text) 
        # for char, countc in char_counts.items(): # Removed print to return dict. 
        #    print(f"{char}: {countc}")
    return char_counts


def char_count(text):
    # This function iterates through each character in the input text, 
    # converts it to lowercase, and checks if it's an alphabetic character 
    # using the isalpha() method. It then updates a dictionary to keep 
    # track of the count for each unique character. The get() method is used 
    # to retrieve the current count for a character, defaulting to 0 if it 
    # hasn't been seen before. Finally, the function returns the dictionary 
    # containing the character counts. 
    count = {} 
    for char in text.lower(): # converting to lower via the string.lower()
        if char.isalpha(): 
            count[char] = count.get(char, 0) + 1 
    return count

# Report takes path/file, letters' dictionary, and total word count and formats 
# into a report per instructions.
def produce_report(title, numbers, total): 
    print(f"{'-' * 50}") 
    print(f"--- Begin report of {title} ---") 
    print(f"{'-' * 50}")
    print(f"{total} words found in the document")
    print(f"{'-' * 50}")
 
    sorted_numbers = dict(sorted(numbers.items(), key=lambda item: item[1], reverse=True))

    for key, value in sorted_numbers.items():
        print(f"The '{key}' character was found {value} times")
    print(f"--- End report ---")


# Run the script's functions ie. Get to work!
main()