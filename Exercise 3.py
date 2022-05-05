n = 18

# No of Guesses 7

# print No of guesses left
# No of guesses he took to finish
# Game Over

guess = int(input("Enter Your Guessing Number: "))
level = 0

while guess > n and level != 9:
    print("Guess Number is Greater")
    guess = int(input("Enter Your Guessing Number: "))
    while guess == n and level != 9:
        print("You are Winner")
        exit()
    while guess < n and level != 9:
        print("Guess Number is Smaller")
        guess = int(input("Enter Your Guessing Number: "))

while guess == n and level != 9:
    print("You are Winner")
    exit()
    while guess > n and level != 9:
        print("Guess Number is Greater")
        guess = int(input("Enter Your Guessing Number: "))
    while guess < n and level != 9:
        print("Guess Number is Smaller")
        guess = int(input("Enter Your Guessing Number: "))

while guess < n and level != 9:
    print("Guess Number is Smaller")
    guess = int(input("Enter Your Guessing Number: "))
    while guess > n and level != 9:
        print("Guess Number is Greater")
        guess = int(input("Enter Your Guessing Number: "))
    while guess == n and level != 9:
        print("You are Winner")
        break


