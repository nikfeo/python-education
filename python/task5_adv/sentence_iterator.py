import re


class SentenceIterator:
    """Creates class Sentence Iterator to make iterable class Sentence"""

    def __init__(self, words):
        self._words = words
        self._index = 0

    def __next__(self):
        """Method returns the next item in the sequence"""
        if self._index >= len(self._words):
            raise StopIteration
        result = self._words[self._index]
        self._index += 1
        return print(result)


class Sentence:
    """Creates class Sentence"""

    end_symbols = ['.', '!', '?', '...', ]

    def __init__(self, sentence: str):
        self.sentence = sentence
        if not isinstance(self.sentence, str):
            raise TypeError("It is not a string. Please, type string!")
        if sentence[-1] not in self.end_symbols:
            raise ValueError('This is an unfinished sentence. Use end symbols.')

    def __repr__(self):
        """Overloads the method for the new display"""
        return f"<Sentence(word={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __iter__(self):
        """Iterator-terminator! Hasta la vista, baby!"""
        return SentenceIterator(self.words)

    def __getitem__(self, index):
        """Returns word by index"""
        return self.words[index]

    def _words(self):
        """Method implements lazy iterator"""
        for word in re.findall(r"\w+", self.sentence):
            yield word

    @property
    def words(self):
        """Method returns list of the words in sentence"""
        return list(self._words())

    @property
    def other_chars(self):
        """Method returns list of special chars"""
        return re.findall(r'[,.!?_\':;/#%*=@"]', self.sentence)


gandalf_vs_balrog = Sentence('I am a servant of the Secret Fire, wielder of the flame of Anor.')
print(gandalf_vs_balrog)
for i in gandalf_vs_balrog:
    print(i)
print(f"{' '.join(gandalf_vs_balrog[8:])}")
print(gandalf_vs_balrog.words)
print(gandalf_vs_balrog.other_chars)
next(gandalf_vs_balrog._words())
