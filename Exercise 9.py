# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guess too high, too low, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
# Extras
# 1. Keep the game going until the user types "exit"
# 2. Keep track of how many guesses the user has taken, and when the game ends, print this out.

# If we are to use RNG, we need to introduce the module first
import random

# We also need a counter
counter = 0

# keep the program running forever with while True:
while True:
    # Use this syntax to generate random numbers ---> random.randint(start number, end number).
    # start and end are included.
    # creating random in WHILE will make it regenerate everytime the loop resets
    a = random.randint(1, 9)

    # now ask the user to guess something
    guess = int(input("Guess the number (1-9): "))

    # and everytime users guess, add 1 into the counter. We're gonna show it when they exit.
    counter+=1
    # compare the generated number from a with user's guess. Using difference helps differentiate if a or guess is higher.
    if a-guess == 0:
        print("You guessed it!")
    elif a-guess > 0:
        print("You guessed too low")
    else:
        print("You guessed too high")

    # We need to ask the users if they want to stop the program
    conti=input("Type 'exit' to leave the program: ")
    if conti == 'exit':
        print("\nYou've guessed " + str(counter) + " times!")
        break