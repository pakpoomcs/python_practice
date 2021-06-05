# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
# Extras:
# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
c = []

# Look into set B first (the longer set), then see if there is any same number in a
for i in a:
    if i in b and i not in c:
        c.append(i)
    i+=1
print(c)

# Apparently you can use NOT in conditional statements
# I don't really understand this one well