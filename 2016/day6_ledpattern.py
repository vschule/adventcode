from collections import defaultdict
from day3_giftdelivery import Coordinate

class Rectangle:
    def __init__(self, genre):
        self.coordinates = defaultdict(genre)

    def draw(self, function, start, end):
        for y in range(start.y, end.y+1):
            for x in range(start.x, end.x+1):
                coord = Coordinate(x, y)
                value = self.coordinates[coord]
                value = function(value)
                self.coordinates[coord] = value

    def result(self, function):
        return function(self.coordinates.values())



def clean_data(str_input):
    lines = []
    for line in str_input.splitlines():
        words = line.split()
        if words.__len__() == 4:
            operation = words[0]
            words = words[1:]

        elif words.__len__() == 5:
            operation = words[1]
            words = words[2:]

        else :
            raise NotImplementedError

        start = Coordinate(words[0].split(','))
        end = Coordinate(words[2].split(','))
        lines.append((operation, start, end))

    return lines

# Lights in your grid are numbered from 0 to 999 in each direction;
#  the lights at each corner are at 0,0, 0,999, 999,999, and 999,0.
# The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs.
# Each coordinate pair represents opposite corners of a rectangle, inclusive;
#  a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.
# The lights all start turned off.


def first(str_input):
    def toggle(value):
        return not value

    def turn_on(value):
        return True

    def turn_off(value):
        return False

    def result(values):
        return sum(1 for item in values if item == True)

    functions = {'on':turn_on, 'off':turn_off, 'toggle': toggle}
    rect = Rectangle(bool)

    lines = clean_data(str_input)

    for line in lines:
        oper = functions[line[0]]
        rect.draw(oper, line[1], line[2])

    return rect.result(result)


def test_first():

    assert first('turn on 0,0 through 999,999') == 1000000
    assert first('turn off 499,499 through 500,500') == 0
    assert first('toggle 0,0 through 999,0') == 1000
    assert first('turn on 0,0 through 999,999\nturn off 499,499 through 500,500') == 999996

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1,
#  to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

def second(str_input):
    def toggle(value):
        return value + 2

    def turn_on(value):
        return value + 1

    def turn_off(value):
        return max(value - 1, 0)

    def result(values):
        return sum(values)


    functions = {'on': turn_on, 'off': turn_off, 'toggle': toggle}
    rect = Rectangle(int)

    lines = clean_data(str_input)

    for line in lines:
        oper = functions[line[0]]
        rect.draw(oper, line[1], line[2])

    return rect.result(result)


def test_second():
    assert second('turn on 0,0 through 0,0') == 1
    assert second('toggle 0,0 through 999,999') == 2000000


if __name__ == '__main__':
    # test_first()
    test_second()

    with open('input_6.txt', 'r') as input_file:
        input_value = input_file.read()

    # print("first problem :", first(input_value))
    print("second problem:", second(input_value))


