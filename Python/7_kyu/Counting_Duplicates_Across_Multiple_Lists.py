# Given a multiple lists(name, age, height), each of size n:

# An entry contains one name, one age and one height. The attributes
# corresponding to each entry are determined by the index of each list, for
# example entry 0 is made up o name[0], age[0], height[0].

# A duplicate entry is one in which the name, age and height are ALL the same.

# Write a function count_duplicated(name, age, height) which takes in the
# attributes for each entry and reutns an integer for the number of duplicated
# entries. For a set of duplicated, the oginal entru should not be counted as a
# duplicate.

def count_duplicated(name, age, height):
    count = 0
    dup = []
    for i,j,k in zip(name, age, height):
        if (i,j,k) not in dup:
            dup.append((i,j,k))
        else:
            count += 1
    return count
