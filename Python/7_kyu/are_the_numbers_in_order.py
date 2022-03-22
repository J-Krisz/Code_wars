# In this Kata, your function receives an array of integers as inpyt. Your task
# is to determine wether the numbers are in ascending order. An array is said
# to be in ascending order if there are no two adjacent integers where the left
# integer exceeds the right integer in value.

# For the purpose of this Kata, you may assume that all inpurs are velid, i.e.
# non-empty arrays containing only integers.

# Note tha tan array of 1 integer is autmatically considered to be sorted in
# ascending order since all (zero) adjacent pairs of integers satisfy the
# condition that the left integer does not exceed the righ integer in value. An
# empty list is considered a degenerate case and therefore will not be tested
# in this Kata - feel free to reise an issue if you see such a list being
# tested.

# For example 
    # in_asc_order([1,2,4,7,19]) # returns True
    # in_asc_order([1,6,10, 18,2,4,20]) # return False


def in_asc_order(arr):
    return arr == sorted(arr)
