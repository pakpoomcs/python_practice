# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Hint: remember to use the user input lessons from the very first exercise

import random

exit = ['EXIT','EXIt','EXiT','ExIT','eXIT','EXit','ExiT','exIT','eXIt','eXiT','eXiT','exiT','exIt','eXit','exit']

confirm = ['Y','y','Yes','yes','YES','YEs','YeS','yES','yeS','yEs']
refuse = ['N','n','NO','No','nO','no']

def generate_rando():
    x = random.randint(0, 9)
    print('The number has been generated. Guess what it is.')
    while True:
        guess = input("Guess the number: ")
        if int(guess) < x:
            print("Too low!")
        elif int(guess) > x:
            print("Too high!")
        elif int(guess) == x:
            print("You guessed it!")
        elif guess in exit:
            break


while True:
    prompt = input("One more round? [y/n]")
    if prompt in confirm:
        generate_rando()



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