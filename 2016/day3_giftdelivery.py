# He begins by delivering a present to the house at his starting location,
#  and then an elf at the North Pole calls him via radio and tells him where to move next.
# Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
# After each move, he delivers another present to the house at his new location.

from functools import reduce
from collections import defaultdict

PARSE_COORD = {'^': [1, 0], 'v': [-1, 0], '>': [0, 1], '<': [0, -1]}


class Coordinate:
    def __init__(self, arg1, arg2=None):
        if isinstance(arg1, list):
            self.x = int(arg1[0])
            self.y = int(arg1[1])

        else :
            self.x = int(arg1)
            self.y = int(arg2)

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return "{0}:{1}".format(self.x, self.y)


def first(str_input):
    coord_dict = defaultdict(int)
    last = Coordinate(0, 0)

    coord_dict[last] = 1

    for value in str_input:
        last = last + Coordinate(PARSE_COORD[value])
        coord_dict[last] += 1

    return coord_dict.__len__()


def second(str_input):
    coord_dict = defaultdict(int)

    santa = Coordinate(0, 0)
    robot_santa = Coordinate(0, 0)

    coord_dict[santa] = 2

    enum = enumerate(str_input)
    for key, value in enum:
        santa = santa + Coordinate(PARSE_COORD[value])
        coord_dict[santa] += 1

        key, robot_value = enum.__next__()
        robot_santa = robot_santa + Coordinate(PARSE_COORD[robot_value])
        coord_dict[robot_santa] += 1

    return coord_dict.__len__()


def test_first():
    assert first('>') == 2
    assert first('^>v<') == 4
    assert first('^v^v^v^v^v') == 2


def test_second():
    assert second('^v') == 3
    assert second('^>v<') == 3
    assert second('^v^v^v^v^v') == 11


if __name__ == '__main__':
    test_first()
    test_second()

    with open('input_3.txt', 'r') as input_file:
        input_value = input_file.read()

    print(first(input_value))
    print(second(input_value))
