def main():
    # If the user enters Hard or Casual, the 'not' operator will return False. The code block will not run, and the rest of the program will continue. If the user enters 'Easy' or something that is NOT 'Hard' or 'Casual', the 'not' operator will return True, and the code block will run printing "Enter a valid difficulty" and the program will end.
    difficulty = input("Hard or Casual? ")
    if not (difficulty == "Hard" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return


   # Same story here. If the user enters 'Multiplayer' or 'Singleplayer', the 'not' operator will return False, and the code block will not run. If the user enters something that is NOT 'Multiplayer' or 'Singleplayer', the 'not' operator will return True, and the code block will run printing "Enter a valid number of players" and the program will end.
    players = input("Multiplayer or Singleplayer? ")
    if not (players == "Multiplayer" or players == "Singleplayer"):
        print("Enter a valid number of players")
        return
    
    if difficulty == "Hard" and players == "Multiplayer":
            recommend("Poker")
    elif difficulty == "Hard" and players == "Singleplayer":
         recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
         recommend("Hearts")
    else:
        recommend("Clock")




def recommend(game):
    print("You might like", game)


main()