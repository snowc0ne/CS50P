# Implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
# Convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    time = input("What time is it? ")
    convert(time)


def convert(time):
    # The time is in the format of hours:minutes. We need to convert the minutes to hours to get the total time in hours.
    # We can do this by dividing the minutes by 60. For example, if the time is 7:30, we can convert the minutes to hours by dividing 30 by 60. 30/60 = 0.5. So the total time in hours is 7 + 0.5 = 7.5.
    # We can get the hours by getting the string up to the colon. We can get the minutes by getting the string after the colon.
    # We can get the string up to the colon by using time.index(":"). We can get the string after the colon by using time.index(":")+1. We can convert the minutes to hours by dividing the minutes by 60.
    # time.index("") finds the position of a character in a string. time.index(":") will give us the index of the colon. So if the time is 7:30, the colon is at index 1. So time.index(":") will give us 1.
    hours = float(time[:time.index(":")]) # The : before time.index's argument is to get the string up to the colon. So if the time is 7:30, the hours will be 7. The colon is at index 1, so the string up to the colon is 7.
    minutes = float(time[time.index(":")+1:])/60 # The +1 is to skip the colon. The /60 is to convert minutes to hours (since there are 60 minutes in an hour). So if the time is 7:30, the minutes will be 0.5. 30/60 = 0.5. Putting the : at the end is to get the rest of the string after the colon. So if the time is 7:30, the minutes will be 30. The colon is at index 1, so the rest of the string after the colon is 30.
    # If we did not include the +1 in time.index(":")+1: then we would get the colon as well. So if the time is 7:30, the minutes would be :30. The colon is at index 1, so the rest of the string after the colon is :30. We do not want the colon, so we need to skip it by adding 1 to the index.
    time = hours + minutes

    if time >= 5 and time < 12:
        print("Breakfast")
    elif time >= 12 and time < 18:
        print("Lunch")
    elif time >= 18 and time < 24:
        print("Dinner")
    else:
        print("not meal time")


if __name__ == "__main__":
    main()