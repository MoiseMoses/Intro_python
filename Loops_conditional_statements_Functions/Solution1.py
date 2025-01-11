"""
Write a Python script that will determine the result of a rock, paper, scissors game,
given Player 1 and Player 2’s choice"""


def play_game(answer1,answer2):   

    if(answer1 == "Paper" and answer2 == "Rock") or (answer1 == "Scissors" and answer2 == "Paper") or\
        (answer1 == "Rock" and answer2 == "Scissors"):
        print(answer1, answer2)
        print("Player 1 wont the game")

    elif answer1 == answer2:
        print(answer1, answer2)
        print("This game is a draw")

    else:
        print(answer1, answer2)
        print("Player 2 wont the game")

if __name__ == "__main__":
  
    CHOICE = ["Rock", "Paper", "Scissors"]
    print("This is the rock, paper, scissors game")
    print("The result will depend on the choice of each of the 2 players")
    print()
    # I use the while statement to force players to only make a choice among  the element in the  CHOICE list
    while True:
        answ1 = input("Player 1, please make your choice (Rock, Paper, or Scissors): ")
        if answ1 in CHOICE:
            break  # Exit the loop if the input is valid
        else:
            print("You are making a wrong choice, it must be Rock, Paper, or Scissors")
    print()
    while True:
        answ2 = input("Player 2, please make your choice (Rock, Paper, or Scissors): ")
        if answ2 in CHOICE:
            break  # Exit the loop if the input is valid
        else:
            print("You are making a wrong choice, it must be Rock, Paper, or Scissors")

print(play_game(answ1,answ2))