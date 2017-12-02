# An opening parenthesis, (, means he should go up one floor, and
# a closing parenthesis, ), means he should go down one floor.
PARSE_FLOOR = {'(': 1, ')': -1}


def first(str_input):
    floor = 0
    for value in str_input:
        floor += PARSE_FLOOR[value]

    return floor

# Now, given the same instructions,
# find the position of the first character that causes him to enter the basement (floor -1).
# The first character in the instructions has position 1, the second character has position 2, and so on.


def second(str_input):
    floor = 0
    for key, value in enumerate(str_input):
        floor += PARSE_FLOOR[value]
        if floor == -1:
            break

    return key+1


def test_first():
    assert first('(())') == 0
    assert first('()()') == 0
    assert first('(()(()(') == 3
    assert first('))(((((') == 3
    assert first('))(') == -1
    assert first(')())())') == -3


def test_second():
    assert second(')') == 1
    assert second('()())') == 5
    assert second('()))') == 3


if __name__ == '__main__':
    test_first()
    test_second()

    with open('input_1.txt','r') as input_file:
        input_value = input_file.read()

    print(first(input_value))
    print(second(input_value))
