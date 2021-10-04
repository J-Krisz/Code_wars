# Create a function that accepts 2 string arguments and returns an integer of
# the count of of occurances the 2nd argument is found in the first one. If no
# occurences can be found, a count of 0 should be returned 

    # ('Hello', 'o') => 1
    # ('Hello', 'l') => 2
    # ('', 'z') => 0

# Notes:
    
    # The first argument can be an empty string
    # The second string argumnet will always be of length 1


def str_count(strng, letter):
    return strng.count(letter)
