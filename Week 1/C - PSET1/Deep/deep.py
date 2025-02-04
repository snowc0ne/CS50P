def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Checks if the user's input is not equal to "42", "forty-two", or "forty two". If the user's input is not equal to any of these, the code block will run printing "No" and the program will end. If the user's input is equal to "42", "forty-two", or "forty two", the 'not' operator will return False, and the code block will not run. The program will continue.
    if not (answer == "42" or answer == "forty-two" or answer == "forty two"):
        print("No")
        return
    else:
        print("Yes")

main()