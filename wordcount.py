# Written by Kevin Bishop

import operator
import string

# These are all of our legal characters that can be in words
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


"""This takes in a text blob and counts the words in it, returning a list of
the top ten most frequently occuring ones. Ties will be arbitrarily decided.
First, the text blob is tokenized with the tokenize() method. The words
are all counted and stored in a dictionary, which is then sorted in 
descending order of keys. The top ten in this list are returned.

Keyword arguments:
string text_blob -- An input string of text to be analyzed

returns list -- A list of the top ten most occuring words.
"""
def wordcount(text_blob):
    #TODO Add a check to ensure text_blob is a string?
    words = tokenize(text_blob)
    top_ten = []
    word_count = {}
    # Count up all the words
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Sort them in descending order of occurence
    sorted_words = sorted(word_count.items(), key=operator.itemgetter(1),
                          reverse=True)

    for i in range(0, 10):
        top_ten.append(sorted_words[i][0])

    return top_ten

print wordcount("cat cat dog dog moose goat goat")
