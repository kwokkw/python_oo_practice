# Inheritance
from wordfinder import WordFinder
from random import choice


class SpecialWordFinder(WordFinder):
    """Specialized Word Finder that excludes blank lines and comment that's start with # symbol.

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def read_file(self, file):
        return [
            word.strip() for word in file if word.strip() and not word.startswith("#")
        ]


f = SpecialWordFinder("new_words.txt")
# print(f)
