# Written by Kevin Bishop

import wordcount

# Test base case
def test_tokenize_1():
    assert wordcount.tokenize('Hello World!') == ['Hello', 'World']
    assert wordcount.tokenize('Hello World!') != ['World', 'Hello']

# Test both letters and numbers
def test_tokenize_2():
    assert wordcount.tokenize('He110 W0R1D') == ['He110', 'W0R1D']

# Test for non ascii letters and numbers
def test_tokenize_3():
    assert wordcount.tokenize('12.34\nabc.def/ghi\'jkl!mno@pqr#stu$vwx%yz..  '
                             ) == ['12', '34', 'abc', 'def', 'ghi', 'jkl',
                                   'mno', 'pqr', 'stu', 'vwx', 'yz']

# Test empty string returns empty list
def test_tokenize_4():
    assert wordcount.tokenize('') == []
