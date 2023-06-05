import random
w1 = 0
w2 = 0


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
    elif (player =="rock" and computer=="scissors") or (player == "scissors" and computer =="paper") or (player== "paper" and computer=="rock"):
            w1=w1+1
            print("You Win!")
    else:
            w2=w2+1
            print("You Lose!")


    print(f"Score is Player/Computer:", w1, "/", w2 )


    play_again = input("Do you wish to play again? (Yes/No): ").lower()
    if play_again != "yes":
        break

print(f"Final score(Player - Computer):",w1,w2)