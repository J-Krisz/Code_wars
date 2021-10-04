# 6 Kyu
# 1. Your message is a string containing space saparated words.
# 2. You need to encrypt each word in the message using the following rules:
    # The first letter must ve converted to its ASCII code.
    # The second letter must be swithced with the last letter
# 3. Keepin' it simple: There are no specia characters in the input.


def encrypt_this(text):

    string_list = text.split(' ')
    text_list = list()
    for word in string_list:
        if len(word) == 1:
            first_letters_ASCII = str(ord(word))
            text_list.append(first_letter_ASCII)
        elif len(word) == 2:
            first_letter_ASCII = str(ord(word[0]))
            cypher = first_letter_ASCII + word[1]
            text_list.append(cypher)
        elif len(word) > 2:
            first_letter_ASCII = str(ord(word[0]))
            cypher = first_letter_ASCII + word[-1] + word[2:-1] + word[1]
            text_list.append(cypher)
        else:
            text_list.append('')

    return ' '.join(text_list)
