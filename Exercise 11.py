# Ask the users for a number and determine whether the number is prime or not.


#a = [x for x in range(2, num) if num % x == 0]

# Now to define a function
def is_prime():
    # First create an input prompt
    num = int(input("What's the number? "))

    # then create a variable to determine if the input can be divided evenly from 2 to input-1.
    # Prime number can be evenly divided by 1 and itself. So this statement will give us the list of the
    # correct divisors, excluding itself.
    # That means prime numbers will generate an empty list. So, len(a) == 0
    a = [x for x in range(2, num) if num % x == 0]

    if num>0:
        if len(a) == 0:
            print(str(num)+" is a prime number.")
        else:
            print(str(num)+" is a composite number.")
    else:
        print(str(num)+" is not a prime number because it is less than or equal to 0.")

no = ['n','N', 'no', 'NO','No','nO']

while True:
    is_prime()
    ask=input("Do you want to continue? (y/n) ").lower()
    if ask in no:
        break

