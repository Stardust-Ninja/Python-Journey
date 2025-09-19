import random
player = input ("wat is je keuze: ")
keuze = ["steen", "papier", "schaar"]
computer = random.choice(keuze)
print("computer kiest", computer)

if player == computer:
    print("gelijkspel")
elif player == "steen" and computer == "schaar":
    print("je wint")
elif player == "papier" and computer == "steen":
    print("je wint")
elif player == "schaar" and computer == "papier":
    print("je wint")
else:
    print("computer wint")
