# If x is divisible by 2. % is the modulo operator which returns the remainder of the division of the number to the left by the number on its right. If the remainder is 0, then the number is even. Otherwise, it is odd.


def main():
    x = int(input("What's x? "))
    if is_even(x): # If this modulo function returns True, then it will print "Even"
        print("Even")
    else:
        print("Odd")


# If the number is divisible by 2 with a remainder of 0, then it will return True. This function is checking if the number is even or not
def is_even(n):
    return n % 2 == 0 # This only has two answers, True or False. The answer gets returned to the main function where it was called.
    
# This is the same as the code below and above
    # return True if n % 2 == 0 else False


# This is the same as the code above
    # if n % 2 == 0: 
    #     return True
    # else: 
    #     return False

main()








# 1st example of old code from the lecture


# if x % 2 == 0: 
#     print("Even")
# else:
#     print("Odd")