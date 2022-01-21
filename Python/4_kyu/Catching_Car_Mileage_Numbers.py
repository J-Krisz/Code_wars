# ""7777...8?!?!", exclaimed Bob, "I missed it again!"Argh!" Every time there's an
# interesting number coming up, he notices and the promptly forgets. Who does
# not like catching those one-off interesting mileage numbers?"

# Let's make it so Bob never misses another interesting number. We've hacked
# into his car's computer, and we have a box hooked up that reads mileage
# nubmers. We've got a box glued to his dash that lights up yellow or green
# depending on wether it receives a 1 or a 2 (respectively)

# It's up to you, intrepid warrior, to glue the parts together. Write the
# function that parses the mileage number inupt, and returns a 2 if the number
# is "interesting" (see below), a 1 if an iteresting number occures withing the
# next two miles, or a 0 if the number is not itneresting.


######################
# INTERESTING NUMBERS#
######################

# interestign numbers are 3-or-more digit numbers that meet one or more if the
# following criteria:

        # Anu digit followed by all zeros: 100, 9000
        # Every digit is the same number: 1111
        # The digits are sequential, incrementing: 1234
        # The digits are sequential, decrementing: 4321
        # The digits are a palindrome: 1221 or 73837
        # The digits match one of the values in the awesome_phreses array

    # + For incrementing sequences, 0 should come after 0, and bot before 1, as
    # in 7890

    # ++ for devrementing sequences, 0 should come after 1, and not before 9,
    # as in 3210


##################
# ERROR CHECKING #
##################

    # A number is only interesting if its is greater than 99!
    # Inpyt will always be an integer greater than 0, and less than 1,000,000,
    # 000
    # The awesomePhrases array will always be provided, and will always be an
    # array, but may be wmpty. (Not everyone thins numbers spell funny words
    # ...)
    # You should only ever output 0,1 or 2


from functools import reduce

def is_interesting(number, awesome_phreses):
    criteria = [
            is_followed_by_0,
            is_same_number,
            is_seq_incrementing,
            is_seq_decrementing,
            is_palindrome,
            is_awesome_phrases
            ]
    
    return reduce(lambda x, y: y(x), criteria, str(number)

def is_followed_by_0(num):
    return num[1:] == (len(num) - 1) * '0'

def is_same_number(num):
    return num == num[0] * len(num)

def is_seq_incrementing(num):
    return ''.join(num.split().sort()) == num

def is_seq_decrementing(num):
    return ''.join(num.split().sort(reversed=True)) == num

def is_palindrome(num):
    return num == num[::-1]

def is_awesome_phrases(num, phrases):
    # for phrase in phrases:
    #     if num is phrase:
    #         return True
    # return False
    return num == phrase for phrase in phrases















