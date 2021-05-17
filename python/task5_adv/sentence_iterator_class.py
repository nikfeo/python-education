class SentenceIterator:
    """Creates class Sentence Iterator to make iterable class Sentence"""

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        """Method returns the next item in the sequence"""
        try:
            part = self.words[self.index]
        except IndexError as error:
            raise StopIteration("Stop iteration") from error
        self.index = self.index + 1
        return part


class Sentence:
    def __init__(self, text: str):
        pass

    def __repr__(self):
        return f"<Sentence(words={?}, other_chars={?})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def _words(self):
        return <lazy iterator>

    @property
    def words(self):
        return words in text\

    @property
    def other_chars(self):
        return not words