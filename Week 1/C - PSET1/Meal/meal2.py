def main():
    meal = input("What time is it? ")
    convert(meal)


def convert(meal):
    hours, minutes = meal.split(":") # Split the string into two parts, the hours and the minutes. The split function splits a string into a list of strings. The split function takes a string as an argument. The string is the character that the string will be split by. So if the string is "7:30", the split function will split the string into two strings, "7" and "30". The colon is the character that the string will be split by.
    hours = float(hours)
    minutes = float(minutes) / 60
    time = hours + minutes

    if time >= 5 and time < 11:
        print("It's breakfast time!")
    elif time >= 11 and time < 14:
        print("It's lunch time!")
    elif time >= 14 and time < 20:
        print("It's dinner time!")
    else:
        print("Not time to eat fatty")

if __name__ == "__main__":
    main()

