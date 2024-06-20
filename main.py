def main():

    # reads the whole frankenstein book
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # takes total_words and calls the count_words function with file_contents as the parameter
    total_words = count_words(file_contents)
    print(total_words)

    #prints the total amount of characters in the frankenstein book
    total_characters = count_characters(file_contents)
    print(total_characters)
    
    
# looks at the whole book and counts the number of words
def count_words(file_contents):
    total_words = file_contents.split()
    return len(total_words)

def count_characters(file_contents):
    lowercase_words = file_contents.lower()
    each_character = {}

    #iterates through each character in the string and adds it to the each_character dictionary if not already there
    for char in lowercase_words:
        if char in each_character:
            each_character[char] += 1
        else:
            each_character[char] = 1
    return each_character
            
main()


