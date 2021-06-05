# Write a program that asks the user how man Fibonacci numbers to generate and the generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonacci sequence is a sequence of numbers where the next number is the sum of the previous two.

# First we create an empty list first
fib = []

# Next, create a function that determine the sequence
def fibo():
    real_num = int(input("How many sequences do you want? "))
    # subtract 1 from the input so we give the correct number of sequence
    num = real_num-1
    i = 1
    # if user wants just one sequence, give him [1]
    if num == 1:
        fib = [1]
    # if user wants two sequences, give [1,1]
    elif num == 2:
       fib = [1,1]
    # more than two sequence can be calculated using the statements below
    elif num > 2:
        fib = [1,1]
        while i < num:
            fib.append(fib[i]+fib[i-1])
            i+=1
    return fib

# Show the result
print(fibo())