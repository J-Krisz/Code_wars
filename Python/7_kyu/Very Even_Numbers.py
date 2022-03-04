# Task 

# Write a function that returns 'true' if the numbe is a "Very Even" number.
# If a number is a single digit, then it is simply "Very Even" if it itself is
# even. 
# If it has two or more digigits, it is "Very Even" if the sum of its digits is
# "Very Even".

    # Examples 

        # number = 88 => return False -> 8+8 = 16 -> 1+6 = 7 => 7 is odd

        # number = 222 => return True -> 2+2+2 = 6 => 6 is even

        # number = 5 => return False 

        # number = 841 => return True -> 8+4+1 = 13 -> 1 + 3 => 4 is even

# Note: The nubmers will always be 0 or positive integers!


def is_very_even_number(n):
    if n < 10:
        return n % 2 == 0

    return is_very_even_number(sum(int(d) for d in str(n)))

















