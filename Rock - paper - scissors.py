import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("choose rock, paper or scissors: ").lower()

    print("You choose ", player)
    print("the computer has choose: ", computer)

    if player == computer:
            print("we have a draw!")
    elif (player =="rock" and computer=="scossor") or (player == "scissor" and computer =="paper") or (player== "paper" and computer=="rock"):
            print("You Win")
    else:
            print("You Lose!")
    play_again = input("Do you wish to play again? (Y/N): ").lower()
    if play_again != "y":
        break