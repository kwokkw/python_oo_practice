import random


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, file):
        self.file = file

    def read_file(self):
        with open(self.file, "r") as file:
            content = [word.strip() for word in file.readlines()]
        return content

    def random(self):
        content = self.read_file()
        return random.choice(content)


rand_word = WordFinder("words.txt")
# print(rand_word.random())

""" NOTE

content = file.readlines() # return a list of words with `\n` attached
content = file.readline()  # read a single line
content = file.read()  # reads the entire content

 """
