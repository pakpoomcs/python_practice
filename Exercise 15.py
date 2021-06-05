#Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string: My name is Michele. Then I would see the string: Michele is name My.

# First, get an input
sen10s = input("Give me a sentence: ")

# Using command .split() to literally split each word in a sentence and turn them into a list.
split = sen10s.split()

# Indexing with [::-1] will reverse the order of the thing.
print(split[::-1])