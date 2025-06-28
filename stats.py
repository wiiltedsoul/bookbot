def count_words(get_book_text):
    words = get_book_text('books/frankenstein.txt').split() # Split the book text into words
    num_words = len(words) # Count the number of words
    return num_words # Return the number of words counted

def character_count(get_book_text):
    text = get_book_text('books/frankenstein.txt').lower() # Get the book text
    characters = {} # Initialize an empty dictionary to count characters
    for chr in text:
        if chr in characters: # Check if the character is already in the dictionary
            characters[chr] += 1
        else:
            characters[chr] = 1
    return characters # Return the character count dictionary

def sort_on(character):
    return character # Return the sorted character count
def sort_characters(get_book_text):
    counts = character_count(get_book_text) # Get the character count dictionary
    char_list = [] # Initialize an empty list to store characters
    for letter in counts: # Iterate through each character in the character count dictionary
        num = counts[letter]
        char_list.append({"char": letter, "num": num}) # Append the character and its count to the list
    char_list.sort(key=lambda d: d["num"], reverse=True) # Sort the list by character count in descending order
    return char_list # Return the sorted character list