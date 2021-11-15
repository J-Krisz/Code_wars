# Kate likes to count words in thext blocks. Bu words she means continuous
# sequences of English alphabetic characters (from a to z). Here are examples

    # `Hello there, little user5453 374 ())$. I'd been using my sphere as a stool.
    # Slow-moving targer 839342 was hit by OMGd-63 or K4mp.` conains "words"
    # `['Hello', 'therre', 'little', 'user', 'I', 'd', 'been', 'using', 'my',
    # 'sphere', 'as', 'a', 'stool', 'Slow', 'moving', 'target', 'was', 'hit',
    # 'by', 'OMGd', 'or', 'K', 'mp']`

# Kate doesn't like some of words and doesn't count them. Words to be excluded
# are 'a', 'the', 'on', 'at', 'of', 'upon', 'in' and 'as', case-insensitive.

# Today Kate's too lazy and have decided to reach her compyter to count "words"
# for her.



EXAMPLE_INPUT_1 = 'Hello there, little user 5453 374())$.'
# Example output 1 == 4

EXAMPLE_INPUT_2 = '''
    I'd been using my sphere as a stool. I traced counterclockwise circles on
    it with my fingertips and it shrank until I could palm it. My bolt had
    shifted while I'd been sitting. I pulled it up and yanked the pleats
    straight as I careered around tables, chairs, globes, and slow-moving
    fraas. I passed under a stone arch into the Scriptorium. The place smelled
    richly of ink. Maybe it was because an ancient fraa and his two fids were
    copying our books there. But I wondered how long it would take to stop
    smalling that way if no one ever used it at all; a lot of ink had been
    spent there, and the wet smell of it must be deep into everything.
'''
# Example output 2 == 112

def word_counts(s):
    pass
