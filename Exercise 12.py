# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25] and makes a new list of only
# the first and the last elements of the given list. For practice write this code inside a function.

a = [5, 10, 15, 20, 25]
b = []

def new_list():
    b.append(a[0])
    b.append(a[-1])
    print(b)
    return b

new_list()