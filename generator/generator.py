from collections import abc

test_list = [1, 2, 3]
assert hasattr(test_list, '__iter__')
assert isinstance(test_list, abc)

class WordSplitIter(object):
    def __init__(self, word):
        self._idx = 0
        self._text = word.split(" ")

    def __repr__(self):
        return f"word split list: {self._text}"

    def __next__(self):
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration("no more index!")
        self._idx += 1
        return word
    
    def __iter__(self):
        print("__iter__ is called")
        return self

class WordSplitGenerator(object):
    def __init__(self, word):
        self._text = word.split(" ")
    
    def __repr__(self):
        return f"word split list: {self._text}"
    
    def __iter__(self):
        for word in self._text:
            yield word
    

