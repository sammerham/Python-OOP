from random import choice 

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        file = open(path)
        self.word_list = self.split_words(file)
        print(f"{len(self.word_list)} words read")
    
    def split_words(self, file):
        """Remove white space and return words in a list."""
        return [word.strip() for word in file]
    
    def random(self):
        """Return Random word from a list"""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    def split_words(self, txt):
        """Remove white space and return words in a list if word isn't white space or starts with #."""
        return [word.strip() 
            for word in txt 
            if word != "" and not word.startswith('#')]
        