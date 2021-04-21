from random import choice 
class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        file = open(path)
        txt = file.read()
        self.word_list = txt.split()
        print(f"{len(self.word_list)} words read")
    
    def random(self):
        return choice(self.word_list)
    
