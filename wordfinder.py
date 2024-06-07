from random import choice


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
        with open(file, "r") as file:
            self.words = self.read_file(file)
        print(f"{len(self.words)} words read")

    def read_file(self, file):
        return [word.strip() for word in file]

    def random(self):
        return choice(self.words)


# rand_word = WordFinder("words.txt")
# print(rand_word)

""" NOTE

content = file.readlines() # return a list of words with `\n` attached
content = file.readline()  # read a single line
content = file.read()  # reads the entire content

 """
