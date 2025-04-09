# Implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str.
# All vanity plates must start with at least two letters. Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters. Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be acceptable. AAA22A would not be acceptable. The first number used cannot be a ‘0’. No periods, spaces, or punctuation marks are allowed. 


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the length of the plate is between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if the plate starts with at least two letters
    if not s[0:2].isalpha():
        return False

    # Check for invalid characters and numbers in the middle
    for i in range(len(s)): # Iterate through each character in the string
        if not (s[i].isalpha() or s[i].isdigit()): # Check if the character is not a letter or digit
            return False # If the character is not a letter or digit, return False
        if s[i].isdigit() and i < len(s) - 1 and s[i + 1].isalpha(): # Checks if the current character is a digit, and if it is not the last character in the string, and if the next character is a letter
            return False

    # Check for leading zero in numbers
    if '0' in s:
        first_digit_index = s.find('0') # Find the index of the first occurrence of '0'
        if first_digit_index > 0 and (first_digit_index == 0 or s[first_digit_index - 1].isalpha()): 
            return False

    return True


main()