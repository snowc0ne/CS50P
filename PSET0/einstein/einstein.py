# Description: This program calculates the energy of an object given its mass. The user inputs the mass of the object in kg and the program calculates the energy of the object using the formula E = mc^2. The speed of light is a constant value of 3 * 10^8 m/s. The program then prints the energy of the object in joules.


def main():
    speed_of_light = 3 * 10**8 #Calculates the speed of light
    mass = int(input("Mass in kg: ")) #Asks the user for the mass of the object and stores it in the variable mass as an integer.
    energy = mass * (speed_of_light ** 2) #Calculates the energy of the object using the formula E = mc^2.

    print(energy)

main() #Calls the main function to run the program.

        