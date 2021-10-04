# 7 Kyu
# You are asked to square every digit and concatenate them.
# For example, if we run 9119 through the funxtion, 811181 will come out,
# bacause 9^2 is 81 and 1^2 is 1.

# Note: The function accepts an integer and returns an integer.

def square_digits(num):
    return "".join([str(pow(int(digit), 2)) for digit in str(num)])


