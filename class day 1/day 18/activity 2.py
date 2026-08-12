# Step 1: Import the random module.
import random
# Step 2: Start a while True loop so the game can repeat for multiple rounds.
while True:
# Step 3: Ask the player for their choice - rock, paper, or scissors.
    choice=int(input("enter your choice rock, paper, or scissors"))
# Step 4: Generate a random number from 1 to 3 using random.randint(1, 3).
    random_number=random.randint(1,3)
# Step 5: Use if/elif to turn that number into the computer's move: 1 becomes rock, 2 becomes paper, and anything else becomes scissors.
    if choice==random_number:
        print("You're still alive")
    elif choice==1 and random_number==2:
        print("You have lost")
    elif choice==2 and random_number==3:
        print("You have lost")
    elif choice==1 and random_number==3:
        print("You have won!")
    elif choice==2 and random_number==1:
        print("You have won")
    elif choice==3 and random_number==1:
        print("You have lost")
    elif choice==3 and random_number==2:
        print("you have won")
# Step 6: Print both the player's and computer's choices using an f-string.
    play_again=input("do you want to play again")
    if play_again!="yes":
        break
# Step 7: Compare the two choices with if/elif to decide whether it's a tie, a win, or a loss, printing the result.

# Step 8: Ask if the player wants to play again, and break out of the loop if the answer isn't "y".