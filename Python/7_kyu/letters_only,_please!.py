# Let's assume we need "clean" strings. Clean means a string should only
# contein letters a-z, A-Z and spaces. We assume that there are no souble
# spaces or line breaks. 

# Write a function that takes a string and returns a string without  the
# unnecessaty characters.

def remove_chars(s):
    return "".join(char for char in s if c.isalpha() or c == " ")
