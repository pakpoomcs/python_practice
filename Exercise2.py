# Ask  a user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: How does an even/odd number react differently when divided by 2?
# Extras:
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#   If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


num=int(input("What the number? "))
# since odd numbers always give the remainder of 1 when divided by 2, we can intepret this 0 or 1 into FALSE or TRUE
if bool(num%2) == False:
    if bool(num%4) == False:
        print(str(num)+" is an even number and can be divided by 4.")
    else:
        print(str(num)+" is an even number but cannot be divided by 4.")
else:
    print(str(num)+" is an odd number")

# For extra number 2, we use % to see whether the remainder is greater than one.
check=int(input("\nNow give me another number: "))
if num%check > 0:
    print(str(check)+" cannot divide evenly into "+str(num))
else:
    print(str(check)+" can divide evenly into "+str(num))