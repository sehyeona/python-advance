from collections import abc

test_list = [1, 2, 3]
assert hasattr(test_list, '__iter__')
# assert isinstance(test_list, abc)

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

def generator_ex1():
    print("start")
    yield "aaa"
    print("continue")
    yield "BBB"
    print("end")

temp = iter(generator_ex1())
for v in temp:
    print(v)
temp2 = [x*2 for x in generator_ex1()]
temp3 = (x*2 for x in generator_ex1())
print(temp2)
print(temp3)

import itertools
gen1 = itertools.count(1, 2.5)
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))
gen3 = itertools.filterfalse(lambda n : n< 3, [1, 2, 3, 4, 5])
gen4 = itertools.accumulate([x for x in range(1, 101)])
gen5 = itertools.chain("ABCDE", range(1, 11, 2))
gen6 = itertools.chain(enumerate("ABCDE"))
gen7 = itertools.product("ABCDE", repeat=2)
gen8 = itertools.groupby("AAABBCCCDDDEEE")

print(next(gen1))
print(next(gen1))
print(next(gen2))
print(next(gen2))
print(next(gen3))
print(next(gen3))
print(next(gen4))
print(next(gen4))
print(gen1, gen2, gen3, gen4, gen5, gen6, gen7, gen8)


