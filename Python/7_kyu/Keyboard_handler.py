# Overview

    # Have you ever wondere how a user interface handles key presses?

    # So today you have the opportunity to create it.

    # Task:
        
        # The keyboard handler is a function which receves three parameters as
        # input:
            # 1. Key - the entered character on the keyboard.
            # 2. isCaps (or is_caps) - boolean variable responsible for the
            # enabled 'Caps Lock'.(by default False)
            # 3. isShift(of is_shift) - boolean variable which is responsible
            # for wether 'Shift' is pressed. (by default False)

        # Your task to write a function that returns the entered character.

        # Requirements for obtaining the #key' variable:
            # Alphabetical characters must ve a lowercase (e.x. 'a', not 'A')
            # it must be a character (e.x #2#, not 2 or not [1,2,3])
            # it must be of unit length (e.x. 'a', not 'abc')

        # if the value does not satisfy the condition, return 'KeyError'

    # For example:

        # handler('a', True) # should return 'A' (because Caps-Lock)
        # handler('1', True) # should return '1' (because Сaps-Lock doesn't work here)
        # handler('a', False, True) # should return 'A' (because Shift)
        # handler('1', False, True) # should return '!'
        
        # handler('')  # should return 'KeyError'
        # handler('A') # should return 'KeyError'
        # handler( 3 ) # should return 'KeyError'
        # handler('abc') # should return 'KeyError'


    # In this kata we use en-US QWERTY layout. (The characters we are working
    # with are shown on a white background)


def handler(key, is_caps=False, is_shift=False):
    return










































