def count_words(text):
    # Split the text into words based on whitespace
    words = text.split()
    # Count the number of words
    word_count = len(words)
    return word_count

def main():
    # Prompt the user to enter a sentence or paragraph
    text = input("Enter a sentence or paragraph: ")
    # Call the function to count words
    num_words = count_words(text)
    # Display the word count
    print("Word count:", num_words)

if __name__ == "__main__":
    main()
