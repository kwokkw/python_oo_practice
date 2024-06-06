# Inheritance
from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):

    def __init__(self, file):
        super().__init__(file)

    def read_file(self):
        content = super().read_file()
        content = [word for word in content if word and not word.startswith("#")]

        # print(content)
        return content

    def random(self):
        return super().random()


f = SpecialWordFinder("new_words.txt")
print(f.random())
