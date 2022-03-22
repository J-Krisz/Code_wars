# You have been hired by a major MP3 player manufacturer to implement a new
# music cimpression standard. In this kata you will implement the ENCODEr, and
# its companion kata deals with the DECODER. It can be considered a herder
# version of 'Range Extraction'

# Specification

    # Asequence of 2 or more identical numvers is hsortened as number*count
    # A sequence of 3 or more consecutive numbers is shortened as first-last.
        # This is true for  both ascending and descending order
    # A sequence of 3 or more numbers with the same inteval is shortened as
    # first-last/interval. Note that the interval does NOT need a sign 
    # Compression happens left to right 


# Examples 
    
    # [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20] is compressed to
        # "1,3-5,7-11,14,15,17-20"

    # [0, 2, 4, 5, 7, 8, 9] is compressed to "0-4/2,5,7-9"

    # [0, 2, 4, 5, 7, 6, 5] is compressed ro "0-4/2,5,7-5"

    # [0, 2, 4, 5, 7, 6, 5, ,5, 5, 5, 5] is compressed ro "0-4/2,5,7-5,5*4"
