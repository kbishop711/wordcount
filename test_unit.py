# Written by Kevin Bishop

import wordcount

# Test base case
def test_tokenize_1():
    assert wordcount.tokenize('Hello World!') == ['hello', 'world']
    assert wordcount.tokenize('Hello World!') != ['world', 'hello']

# Test both letters and numbers
def test_tokenize_2():
    assert wordcount.tokenize('He110 W0R1D') == ['he110', 'w0r1d']

# Test for non ascii letters and numbers
def test_tokenize_3():
    assert wordcount.tokenize('12.34\nabc.def/ghi\'jkl!mno@pqr#stu$vwx%yz..  '
                             ) == ['12', '34', 'abc', 'def', 'ghi', 'jkl',
                                   'mno', 'pqr', 'stu', 'vwx', 'yz']

# Test empty string returns empty list
def test_tokenize_4():
    assert wordcount.tokenize('') == []

# Generic test
def test_wordcount_1():
    with open ('sample_texts/huckleberry.txt', 'r') as f:
        assert wordcount.wordcount(f.read()) == [
            'and', 'the', 'i', 'a', 'to', 'it', 't', 'was', 'he', 'of'
        ]

# Merging two files
def test_wordcount_2():
    blob = ''
    with open ('sample_texts/textfile1.txt', 'r') as f:
        blob += f.read()

    with open ('sample_texts/textfile2.txt', 'r') as f:
        blob = blob + ' ' + f.read()

    assert wordcount.wordcount(blob) == ['this', 'is', 'a', 'test', 'file',
                                         '1', '2', '3', '4', '5']
