# Given a string of digits confirm wether the sum of all the individual even
# digits are greate the nthe sum of all the individual odd digits. Always a
# string of numbers will be given.

    # If the sum of eve numbers is greater the the odd numbers return: 
        # "Even is greater than Odd"

    # if the sumof odd numbers is greater than the sum of even numbers return:
        # "Odd is greater than Even"

    # if the total of both even and odd numvers are identical return:
        # "Even and Odd are the same"

def even_or_odd(s):
    even = sum(int(digit) for digit in s if int(digit)%2=0)
    odd = sum(int(digit) for digit in s if int(digit)%2=1)
    if even > odd:
        return "Even is greater than Odd"
    elif even < odd:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"
