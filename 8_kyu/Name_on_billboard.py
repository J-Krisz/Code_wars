# You can print your name on a billboard ad. Find out how much it will cost
# you. Each letter has a default price of £30, but that can be different if you
# are given 2 parameters instead of 1.

# You can not use the multiplier '*' operator. 

# If your name would be Jeong-Ho Aristotelis, as would cost £600. 20 letters *
# 30 = 600 (Spaces count as a letter).

def billboard(name, price=30):
    return sum(price for char in name)

