# The input is a string str of digits. Cut the string into chinks (a chunk here
# is a substing of the initial string) of size sz (ignore the last chunk
# if its size is less than sz).

# If a chink represents an integer suxh as the sum of the cubes of its digits
# is divisible by 2, reverse that chink; othewise rotate it to the left by on
# position. Put tohether these modified chinls and return the result as a
# string. 

# If

    # sz is <= 0 or if str is empty return ""
    # szis greter (>) than the length of str it is impossible to take achink of
    # a size sz hence return "".


# EXAMPLES:

    # revrot("123456987654", 6) --> "234561876549"
    # revrot("123456987653", 6) --> "234561356789"
    # revrot("66443875", 4) --> "44668753"
    # revrot("66443875", 8) --> "64438756"
    # revrot("664438769", 8) --> "67834466"
    # revrot("123456779", 8) --> "23456771"
    # revrot("", 8) --> ""
    # revrot("123456779", 0) --> "" 
    # revrot("563000655734469485", 4) --> "0365065073456944"
    
    # Example of a string rotated to the left by one position:
    # s = "123456" gives "234561".

def revrot(strng, sz):
    if chunks.isdigit():
        int(chunks)

        if sum(digits for digits in )


def chunks(strn, n):
    return [strn[i:i+ n] for i in range(0, len(strn), n)]


