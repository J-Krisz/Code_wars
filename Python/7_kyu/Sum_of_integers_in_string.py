# Your task in this kata is to implement a function that calculates the sum of
# the integers iside a string. For example, in the string

# The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the
# integers is 3635.

# NOTE: only positive integers will be tested.

def sum_of_integers_in_string(s):
    return sum(int(char) for char in s if char.isdigit())

print(sum_of_integers_in_string("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))