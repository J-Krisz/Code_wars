# Write a function that takes a sstring and an integer 'n' as parameters and
# retuns a list of all words that are longer than n.

# Example:
    # With in[pyt "The quick bown fox jumps over thelazy dog", 4
    # Return ['quick', 'brown', 'jumps']


def filter_long_words(sentence, n):
    return [word for word in sentence.split() if len(word) > n]
