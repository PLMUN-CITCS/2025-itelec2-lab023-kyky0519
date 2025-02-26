def get_sentence_input() -> str:
    """Prompts the user to enter a sentence and returns it."""
    return input("Enter a sentence: ").strip()

def count_words(sentence: str) -> int:
    """Counts the number of words in a given sentence."""
    return len(sentence.split())

def main():
    """Main function to get input, count words, and display the result."""
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} words.")

if __name__ == "__main__":
    main()
