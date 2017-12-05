from collections import defaultdict


class Jumpiterator:
    """ Iterator that breaks when 00000 is found at the start of an md5 hash """

    def __init__(self, instructions, action):
        self.instructions = instructions
        self.length = self.instructions.__len__()
        self.position = 0
        self.action = action

    def __iter__(self):
        self.iteration = 0
        self.position = 0
        return self

    def __next__(self):
        if self.position >= self.length:
            raise StopIteration

        jump = self.instructions[self.position]
        self.instructions[self.position] = self.action(jump)
        self.position = self.position + jump

        self.iteration += 1
        return self.iteration


def first(str_input):
    def increment(value):
        return value+1

    lines = list(map(int,str_input.splitlines()))

    jumps = Jumpiterator(lines, increment)

    for x in jumps:
        continue

    return x


def test_first():
    assert first("0\n3\n0\n1\n-3") == 5


def second(str_input):
    def increment(value):
        if value >= 3:
            return value -1
        return value + 1

    lines = list(map(int, str_input.splitlines()))

    jumps = Jumpiterator(lines, increment)

    for x in jumps:
        continue

    return x


def test_second():
    assert second("0\n3\n0\n1\n-3") == 10

if __name__ == '__main__':
    test_first()
    test_second()

    with open('input_5.txt', 'r') as input_file:
        input_value = input_file.read()

    print("first problem :", first(input_value))
    print("second problem:", second(input_value))
