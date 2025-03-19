# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case. For example, if the user inputs numberOfCollegeGraduates, the output should be number_of_college_graduates. You may assume that the input will contain only letters and no spaces.

def main():
    # Prompt the user for the name of a variable in camel case
    camel_case = input("Enter a variable in camelCase: ")

    # Initialize an empty string to store the snake case version of the variable
    snake_case = ""

    # Iterate over each character in the camel case variable
    for char in camel_case:
        # If the character is uppercase, add an underscore followed by the lowercase version of the character
        if char.isupper():
            snake_case += "_" + char.lower()
        # Otherwise, add the character as is
        else:
            snake_case += char

    # Print the snake case version of the variable
    print(f"snake_case: {snake_case}")


main()