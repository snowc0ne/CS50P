# You are a bank teller. A customer walks in and you greet them. You have to say hello to them as per company policy otherwise you pay them. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    greeting = input("Greeting: ")
    greeting = greeting.strip() #Strips leading and trailing whitespace from the user's input
    greeting = greeting.lower() #Converts the user's input to lowercase

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
