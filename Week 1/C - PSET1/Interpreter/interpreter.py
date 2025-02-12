# Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein: x is an integer y is one of +, -, *, or / and z is an integer



def main():
    expression = input("Expression: ")
    expression = expression.split() #Splits the users input into an array of strings
    x = int(expression[0]) #Converts the first element of the array to an integer
    y = expression[1] #Assigns the second element of the array to a variable
    z = int(expression[2]) #Converts the third element of the array to an integer

    if y == "+":
        print(f"{x} + {z} = {x + z:.1f}")
    elif y == "-":
        print(f"{x} - {z} = {x - z:.1f}")
    elif y == "*":
        print(f"{x} * {z} = {x * z:.1f}")
    elif y == "/":
        print(f"{x} / {z} = {x / z:.1f}")
    else:
        print("Try again")


main()