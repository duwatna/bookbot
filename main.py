def main():

    # reads the whole frankenstein book
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # takes total_words and calls the count_words function with file_contents as the parameter
    total_words = count_words(file_contents)
    print(total_words)
    
# looks at the whole book and counts the number of words
def count_words(file_contents):
    total_words = file_contents.split()
    return len(total_words)

main()


