item = input("Item: ").lower()

fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plum": 70,
    "strawberry": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

if item in fruits:
    print("Calories: ", fruits[item]) # Looks up the item in the dictionary and prints the calories as that is the only value in the dictionary. If there were more values, we would need to specify which one we want to print.





# Ghetto way to do it
# if item == "apple":
#     print("Calories: ", 130)
# elif item == "avocado":
#     print("Calories: ", 50)