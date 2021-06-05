# Write a program (function!) that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

# So here's the list from exercise 5, a and b
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# this loop is to combine a and b together. There will be duplicates but that's what we want.
for i in b:
    a.append(i)
    i+=1
print(a)

# create a function to eliminate the duplicates. we can just use set(x)
def noDup(x):
    return set(x)

# then assign a new variable to the functioned list
dedup=noDup(a)
print("Here's the list without duplication.\n"+str(sorted(dedup)))
# You can even sort it using sorted(x)
