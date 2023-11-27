import random

choices = ["rock","paper","scissors"]

computer = random.choice(choices)
player = None


while player not in choices:
    player = input("Choose: Rock, Paper or Scissors! ").lower()

if player == computer:
    print("Computer chose: "+computer)
    print("Player chose: "+player)
    print("Tie")
elif player == "rock":
    if computer == "paper":
        print("Computer chose: "+computer)
        print("Player chose: "+player)
        print("Player lost\nComputer Won")
    if computer == "scissors":
        print("Computer chose: "+computer)
        print("Player chose: "+player)
        print("Player won\nComputer lost")
elif player == "scissors":
    if computer == "paper":
        print("Computer chose: "+computer)
        print("Player chose: "+player)
        print("Player won\nComputer lost")
    if computer == "rock":
        print("Computer chose: "+computer)
        print("Player chose: "+player)
        print("Player lost\nComputer Won")
elif player == "paper":
    if computer == "rock":
        print("Computer chose: "+computer)
        print("Player chose: "+player)
        print("Player won\nComputer lost")
    if computer == "scissors":
        print("Computer chose: "+computer)
        print("Player chose: "+player)
        print("Player lost\nComputer Won")