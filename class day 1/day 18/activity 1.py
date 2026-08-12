# Step 1: Import the random module.
import random
# Step 2: Set a variable playing to True to control the game loop.
play=True
# Step 3: Generate a secret number between 0 and 9 using random.randint(0, 9), converting it to a string.
number=random.randint(0,9)
# Step 4: Print instructions explaining the guessing game to the player.
while play:
    dice_guess=int(input("enter a number"))
# Step 5: Start a while playing loop that keeps asking for a guess.
    if dice_guess==number:
        print("you have won")
        break
    else:
        print("try again")
# Step 6: If the guess matches the secret number, print a winning message showing the number, then break out of the loop.

# Step 7: Otherwise, print a message asking the player to try again, and the loop continues.