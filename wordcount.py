# Written by Kevin Bishop

import string

CHARS = string.ascii_letters + string.digits

"""This needs to take a text blob and tokenize it into words.
Words are delimited by anything other than a-z, A-Z, or 0-9.

Keyword arguments:
str text_blob -- The input string to be tokenized.

returns list -- A list where each entry is one word. The list should appear
in the same order as in the text blob."""
def tokenize(text_blob):
    #TODO Add a check for text_blob being a string?
    tokens = []
    next_word = ''
    for c in text_blob:
        if c in CHARS:
            next_word += c
        elif next_word != '':
            tokens.append(next_word)
            next_word = ''

    if next_word != '':
        tokens.append(next_word)

    return tokens

results = tokenize("Hello World! This1IS\nA Test....1")
print results
