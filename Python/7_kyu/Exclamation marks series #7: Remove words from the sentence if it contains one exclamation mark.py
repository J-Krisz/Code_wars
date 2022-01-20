# Remove words from the sentence if they contain exactly one exclamation mark.
# Words are separated by a single space, without leading/trailing spaces

## Examples
    # remove("Hi!") == ""
    # remove("Hi! Hi!") == ""
    # remove("Hi Hi!! Hi!") == "Hi Hi!!"

def remove(sentence):
    return " ".join(word for word in sentence.split() if word.count("!") != 1)

