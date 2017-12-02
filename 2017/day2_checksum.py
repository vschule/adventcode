import pytest


def first(lines):
    summed = 0
    for line in lines.splitlines():
        values = list(map(int, line.split()))

        maximum = max(values)
        minimum = min(values)
        summed += maximum - minimum

    return summed


def second(lines):
    output_cs = 0
    for line in lines.splitlines():
        values = list(map(int, line.split()))

        for key, current in enumerate(values):
            found = False

            for value in values[key + 1:]:
                if current % value == 0:
                    result = current / value
                    output_cs += result
                    found = True
                    break

                elif value % current == 0:
                    result = value / current
                    output_cs += result
                    found = True

                    break
            if found:
                break
        if not found:
            raise ValueError

    return int(output_cs)


def test_first():
    assert first("5 1 9 5 \n 7 5 3 \n 2 4 6 8") == 18


def test_second():
    assert second("5 9 2 8 \n9 4 7 3\n3 8 6 5") == 9


if __name__ == '__main__':
    test_first()
    test_second()

    with open("input_2.txt", 'r') as input_file:
        lines_input = input_file.read()

    print(first(lines_input))
    print(second(lines_input))
