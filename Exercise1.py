# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year they will 100 years old.
# Extras:
# 1. Add on to the previous program by asking the user for another number
#   and printing out that many copies of the previous message. (Hint: Order of Operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines.
#   (Hint: the  string \n is the same as pressing the ENTER button.

name=input("What's your name? ")
age=input("How old are you? ")
turning100 = 100-int(age)+2020
times=int(input("Give me another number: "))

print("Hello, "+name+".\nYou're "+age+" years old.")

for i in range(times):
    print("That means you're turning 100 in year "+str(turning100)+"!!!")