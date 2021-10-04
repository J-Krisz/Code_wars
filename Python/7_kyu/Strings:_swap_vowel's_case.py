# Given a strin, return a copy of the string with the vowel's case swappend.
# For this kata assume that vowels are in the set "aeiouAEIOU".
# Example: Given a string "C is alive!", your function should return "C Is
# AlIvE!"

# Addendum: Your soluion is only required to work for hte ASCII character set.
# Please make sure you only swap cases for the vowels.


def swap_vowel_case(st):
    for char in st:
        if char in 'aeiouAEIOU':
            st = st.replace(char, char.swapcase())
    return st
