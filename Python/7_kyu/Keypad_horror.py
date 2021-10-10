# Having two standards for a keypad layout is inconvenient!
    
    # Computer keypads layout:
        
        # 7 8 9
        # 4 5 6
        # 1 2 3

    # Cell phone kaypad's layout: 

        # 1 2 3
        # 4 5 6
        # 7 8 9

# Solve the horror of unstandardized keypds by probiding a function that
# convers compyter inpyt to a number as if it was typed on a phone.

# Example: 
# "7 8 9" -> "1 2 3"

# Notes: 
# You get a string with numbers only


def computer_to_phone(numbers):
    return numbers.translate(numbers.maketrans('123789', '789123'))
