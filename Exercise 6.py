# Snake Water Gun
import random

level = 0
while level == 0 :
    item = ["Snake", "Water", "Gun"]
    computer = random.choice(item)
    user = input("Enter The Key: ")
    
    if user == "s" and computer == "Gun":
        print("\nComputer is Winner")
        print("\nYou is Loser")
        print()

    elif user == "s" and computer == "Water":
        print("\nYou is Winner")
        print("\nComputer is Loser")
        print()

    elif user == "w" and computer == "Sanke":
        print("\nComputer is Winner")
        print("\nYou is Loser")
        print()

    elif user == "w" and computer == "Gun":
        print("\nYou is Winner")
        print("\nComputer is Loser")
        print()

    elif user == "g" and computer == "Snake":
        print("\nYou is Winner")
        print("\nComputer is Loser")
        print()

    elif user == "g" and computer == "Water":
        print("\nComputer is Winner")
        print("\nYou is Loser")
        print()
        level = 6

        

