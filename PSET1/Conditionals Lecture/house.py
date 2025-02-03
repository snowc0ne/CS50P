name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin") 
    case _: # 'case _:' is like 'else'. Whatever case has not been handled
        print("Who?")





# 1st example before 'match'

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")