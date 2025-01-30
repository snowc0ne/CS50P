def main(): #Empty () means this function does not take an input
    msg = input() #Input is a built-in function that takes a string from the user. The input is stored in the variable msg.
    result = convert(msg) #The variable result is assigned the value of the function convert with the input msg.
    print(result)

def convert(msg):
    msg1 = msg.replace(":)", "🙂") #Checks for ':)' in the inputted string and replaces it.
    msg2 = msg1.replace(":(", "🙁") #After the first check is done, it checks for ':(' and replaces it. This way the user can input both :) and :( and it will be converted.
    return msg2 #Returns the converted string.

main() #Calls the main function to run the program.