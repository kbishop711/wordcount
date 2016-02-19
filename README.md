# wordcount
This is an exercise to find the top 10 most occurring words in a text file.

### Installation
This project does not use any specific libraries to be installed. It is
currently tested to work with Python 2.7.x. 

You will need `tox` in order to run the tests. This can be installed with
> pip install tox
or 
> easy_install tox

### Running the script
wordcount takes your text blob argument as a file during runtime. You can 
give it multiple files, and the top 10 words across those files will be
returned. 
> python wordcount.py textfile.txt

> python wordcount.py textfile1.txt textfile2.txt textfile3.txt

Ensure that these input files are in plain-text. A word is defined as any 
continuous string of the characters a-z, A-Z, and 0-9 that is not 
interrupted by any other characters. For example, 'Hello', 'he11O', and '123'
are all considered words, but "Hell.O" would be considered 2 words,
"Hell" and "O". Also, note that for purposes of counting occurrences, words
are case-insensitive.

The program outputs the top 10 words as a list in descending order of
frequency in the text blob:
> ['highest', ... , 'lowest']

### Importing wordcount
You can also import the wordcount class to directly use the functions
`wordcount()` and `tokenize()`. `tokenize()` takes a text blob and returns
a list of possibly repeating words, a tokenization of the text. `wordcount()`
takes a text blob and returns a list of the top 10 most repeating words, in 
the same format as the script output.
