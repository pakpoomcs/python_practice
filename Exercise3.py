# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that prints out all the elements of the list that are less than 5.
# Extras:
# 1. Instead of printing the elements one by one, make a new list that has all the elements less than 5
#   from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the original list 'a'
# that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
s = []

# FOR will assign a variable and look into RANGE to see how often it has repeat.
# In this case, 'i' will be repeated the same amount of the length of 'a'
for i in range(len(a)):
    if a[i]<5:
        s.append(a[i])
        print(s[i])
    i+=1

# Now for extra number 3
d=[]
num=int(input("Give me a number: "))
for i in range(len(a)):
    if a[i]<num:
        d.append(a[i])
        print(d[i])
    else:
        break
    i+=1

# Too bad I couldn't do it in just one line though
