from adv_2015.day3_giftdelivery import Coordinate
from collections import defaultdict

def first(str_input):
    int_input = int(str_input)
    int_input -= 1

    current_values = 1
    i = 0

    while True:
        current_values = current_values + i*8
        if current_values >= int_input:
            break
        i += 1

    result = i
    if int_input != 0:
        int_input += i
        sidestep = int_input % (i*2)
        result = result + sidestep
    return result


class Grid:
    def __init__(self, searched_value):
        self.searched = searched_value
        self.coordinates = defaultdict(int)
        self.moves = [Coordinate(0,1), Coordinate(1,0), Coordinate(0,-1), Coordinate(-1,0),Coordinate(1,1), Coordinate(1,-1), Coordinate(-1,-1), Coordinate(-1,1)]

    def __iter__(self):
        self.iteration = 0
        self.index_direction = 0
        self.change = 1
        self.changed = False
        self.current = Coordinate(0, 0)
        self.coordinates[self.current] = 1

        return self

    def __next__(self):
        if self.iteration == self.change:
            self.iteration = 0
            self.index_direction = (self.index_direction + 1) % 4

            if self.changed:
                self.change +=1
                self.changed = False

            else:
                self.changed = True

        self.current = self.current + self.moves[self.index_direction]

        value = 0
        for move in self.moves:
            neighbour = self.current + move
            value += self.coordinates[neighbour]

        self.coordinates[self.current] = value
        self.iteration += 1
        return value


def second(str_input):

    int_input = int(str_input)
    grid = Grid(int_input)
    grid.__iter__()
    x = 0
    while x <= int_input:
        x = grid.__next__()
    return x


def test_first():
    assert first("1") == 0
    assert first("23") == 2
    assert first("12") == 3
    assert first("1024") == 31


def test_second():
    assert second("1") == 2
    assert second("23") == 25
    assert second("12") == 23
    assert second("800") == 806


if __name__ == '__main__':
    test_first()
    test_second()

    input_value = '277678'

    print("first problem :", first(input_value))
    print("second problem:", second(input_value))
