WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    choice = input("If you want to play, press 1. If you want to see the previous words, press 2: ")
    if choice == "1":
        game()
    elif choice == "2":
        words()

def game():
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            WORDS.clear()
            print("You found the Queen Bee! Good job!")

        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Its all Ogre! Good job! You scored {points} points!")



def words():
    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")


if __name__ == "__main__":
    main()
