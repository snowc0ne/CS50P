def main():
    tweet = input("Input: ")
    vowels = "aeiouAEIOU"
    
    for vowel in vowels: # This will iterate through each vowel individually in the string vowels.
        tweet = tweet.replace(vowel, "") # This will replace all occurrences of the vowel in the tweet with an empty string, effectively removing it.
    print(f"Output: {tweet}")

main()

