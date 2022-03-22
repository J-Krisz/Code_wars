# Given two numbers m and n, such that 0 <= m <= n
    # conver all number from mto n(inclusive) to binary
    # sum them as if the were base 10
    # convert the result to binary
    # return as a string

        # Example
        # 1, 4 --> 11110101 --> 122


def binary_pyramid(m, n):
    return bin(sum([int(bin(i).replace('0b', '')) for i in range(m, \
        n+1)])).replace('0b', '')
