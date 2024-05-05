import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target (or type 'Quit' to exit): ")
    if userChoice.lower() == "quit":
        break

    userChoice = int(userChoice)
    if userChoice == target:
        print("Success: Correct Guess!!")
        break
    elif userChoice < target:
        print("Your guess was too small. Take a bigger guess.")
    else:
        print("Your guess was too big. Take a smaller guess.") 

print("______GAME OVER______")
