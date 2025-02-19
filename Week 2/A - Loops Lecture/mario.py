def main():
    print_column(3)
    print_row(3)
    print_square(3)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    for _ in range(width):
        print("?" * width)




def print_square(size):
    for i in range(size): # This loop will print the number of rows in the square. The number of rows is the size of the square.
        for j in range(size): # This loop will print the number of columns in the square. The number of columns is the size of the square.
            print("#", end="") # The end="" is to prevent the print function from printing a new line. By default, the print function prints a new line after printing the string.
        print()

main()