import random

while True:
    choices = ["earth", "fire", "water", "air"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("earth, fire, water, or air? :").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Draw!")
    elif player == "earth":
        if computer == "fire":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
        if computer == "water":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "air":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
    elif player == "fire":
        if computer == "earth":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "water":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "air":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    elif player == "water":
        if computer == "fire":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
        if computer == "earth":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
        if computer == "air":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
    elif player == "air":
        if computer == "fire":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "water":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
        if computer == "earth":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")

    play_again = input("Play again? (yay/nay): ").lower()

    if play_again != "yay":
        break
print("Sayonara!")
