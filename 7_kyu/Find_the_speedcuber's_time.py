# Speedcubing is the hobby involving solbing a variety of twisty puzzles, the
# most famous being the 3x3x3 puzzle or Rubik's cube, as quckly as possible.

# In the majority of Speedcubing compatitions, a Cuver solves a scrambled cube
# 5 times, and their result is found by taking the average of the middle 3
# solves (ie. the slowest and fastest times are disregarded, and an average is
# taken of the remaining times).

# In some competitions, the unlikely event of a tue is resolve by comparing
# Cuber's fastest times.

# Write a function cube_times(times) that, given an array of floats [times]
# returns an array/tuple with the Cuber's result (to 2 decimal places) AND
# their fastest solve.

# For example:

    # cube_times([9.5, 7.6, 11.4, 10.5, 8.1]) = (9.37, 7.6)
    ## because (9.5 + 10.5 + 8.1) / 3 = 9.37 and 7.6 was the fastest solve.

def cube_times(times):
    times = sorted(times)
    return (round(sum(sorted(times[1:-1]))/3, 2), times[0])
