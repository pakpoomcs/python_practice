# Ask the user for a string and print out whether this string is a palindrome or not.

# First, we need to know the syntax to reverse a string. It's word[len(word)::-1]. Remember this.
word = input("What's the word: ")

# Then we just compare if the word and its reversed self spell the same.
# Here I made both of them lower-cases for easier comparison.
if (word.lower()[len(word)::-1]) == word.lower():
    print(word+" is a palindrome.")
else:
    print(word+" is not a palindrome.")
