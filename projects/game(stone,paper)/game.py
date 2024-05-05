import random
print("THE STONE '🪨'  PAPER '📃' AND SCISSORS '✂' GAME")
rock = '🪨'
paper = "📃"
scissors = '✂'
game_images =[rock,paper,scissors]
user_choice=int(input("Enter Your Choice: \n Type 0 for Rock\n Type 1 for Paper \n Type 2 for scisssors\n"))
print(f"You choose {user_choice}")
if user_choice >=3 or user_choice < 0:
    print("You Entered Invalid number : \n You Lost The Chance")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("Computer Chose:")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("Its a Draw")
    elif computer_choice==0 and user_choice==2:
        print("You Lose")
    elif user_choice == 0 and computer_choice ==2:
        print("You Win")
    elif computer_choice > user_choice :
        print("You Win")
    elif user_choice > computer_choice :
        print("You Win")