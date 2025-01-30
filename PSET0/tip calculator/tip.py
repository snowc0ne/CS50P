# This program calculates the tip for a meal based on the percentage the user wants to tip.

def main (): # This function is the main function that will run the program
    dollars = dollars_to_float(input("How much was the meal? ")) # This calls the dollars_to_float function to convert the input to a float and assigns it to the variable dollars.
    percent = percent_to_float(input("what percentage would you like to tip? ")) # This calls the percent_to_float function to convert the input to a float and assigns it to the variable percent.
    tip = dollars * percent # This calculates the tip by multiplying the dollars by the percent and assigns it to the variable tip.
    print(f"Leave ${tip:.2f}") # This prints the tip to the user with 2 decimal places.


def dollars_to_float(d):
    return float(d.strip('$')) # This function takes a string and removes the dollar sign and converts it to a float.


def percent_to_float(p):
    return float(p.strip('%')) / 100 # This function takes a string and removes the percent sign and converts it to a float and divides it by 100. So if the user enters 20, it will convert it to 0.20.

main() # This calls the main function to run the program.