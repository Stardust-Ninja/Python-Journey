import random
player = input ("what's your choice: ")
choice = ["rock", "paper", "scissors"]
computer = random.choice(choice)
print("computer chose", computer)

if player == computer:
    print("draw")
elif player == "steen" and computer == "schaar":
    print("you win")
elif player == "papier" and computer == "steen":
    print("you win")
elif player == "schaar" and computer == "papier":
    print("you win")
else:
    print("computer wins")



