# The elves are running low on wrapping paper, and so they need to submit an order for more.
# They have a list of the dimensions (length l, width w, and height h) of each present,
# and only want to order exactly as much as they need.

from functools import reduce

def first(str_input):
    lines = str_input.splitlines()

    result = 0

    for line in lines:
        values = list(map(int, line.split('x')))
        result += multiply_box(values)

    return result


def multiply_box(list_values):
    last = list_values[-1]
    areas = []

    for value in list_values:
        areas.append(value*last)
        last = value

    result = sum(areas) * 2 + min(areas)

    return result

# The ribbon required to wrap a present is the shortest distance around its sides,
#  or the smallest perimeter of any one face.
# Each present also requires a bow made out of ribbon as well;
#  the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present.
#  Don't ask how they tie the bow, though; they'll never tell.


def second(str_input):
    lines = str_input.splitlines()

    result = 0

    for line in lines:
        values = list(map(int, line.split('x')))
        values.sort()
        result += (values[0] + values[1]) * 2
        result += reduce((lambda x, y: x * y), values)

    return result


def test_first():
    assert first('2x3x4') == 58
    assert first('1x1x10') == 43
    assert first('2x3x4\n1x1x10') == 101


def test_second():
    assert second('2x3x4') == 34
    assert second('1x1x10') == 14
    assert second('2x3x4\n1x1x10') == 48



if __name__ == '__main__':
    test_first()
    test_second()

    with open('input_2.txt','r') as input_file:
        input_value = input_file.read()

    print(first(input_value))
    print(second(input_value))
