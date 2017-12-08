from collections import defaultdict


class SameTupleIterator:
    def __init__(self, baselist):
        self.tuples = set()

        self.baselist = list(baselist)

    def __iter__(self):
        self.iteration = 1
        return self

    def __next__(self):
        self.iteration +=1
        key, toredistribute = max(enumerate(self.baselist), key=lambda p:p[1])

        self.baselist[key] = 0
        key += 1
        for i in range(0,toredistribute):
            index = (key+i)%self.baselist.__len__()
            self.baselist[index] += 1

        tupled = tuple(self.baselist)
        if tupled in self.tuples:
            raise StopIteration

        self.tuples.add(tupled)
        return  self.iteration, tupled


def first(str_input):
    listinput = list(map(int,str_input.split()))

    resolver = SameTupleIterator(listinput)
    for i, tuple in resolver:
        continue

    return i


def test_first():
    assert first("0 2 7 0") == 5


def second(str_input):
    listinput = list(map(int,str_input.split()))

    resolver = SameTupleIterator(listinput)
    for i, tuple in resolver:
        continue

    resolver = SameTupleIterator(list(tuple))
    for i, tuple in resolver:

        continue

    return i-1


def test_second():
    assert second("0 2 7 0") == 4

    assert second("2 4 1 2") == 4
    return

if __name__ == '__main__':
    test_first()
    test_second()

    with open('input_6.txt', 'r') as input_file:
        input_value = input_file.read()

    print("first problem :", first(input_value))
    print("second problem:", second(input_value))
