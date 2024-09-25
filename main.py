#
# main.py
# 
# Daniel S Cochran
# September 25, 2024 creation date
# 

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count(book_path)
    #char_count(text)
    
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
        print(" *** word count ***")
        print(f"The text file contains {count} words.")

        # Now get the number of times the letter is used in the book (text file)
        char_counts = char_count(text) 
        for char, countc in char_counts.items(): 
            print(f"{char}: {countc}")


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

# Run the script's functions ie. Get to work!
main()