def main():
    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4] # Convert all words to lowercase by iterating over the list of words and using the lower() method on each word. Only include words that are longer than 4 characters.


    counts = {word: lowercase_words.count(word) for word in lowercase_words}


    # for word in lowercase_words:
    #     if word in counts:
    #         counts[word] += 1 # Increment the count of the word by 1
    #     else:
    #         counts[word] = 1

    save_counts(counts)

main()