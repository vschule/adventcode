import pytest
# The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that
# match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the
#  list.


def first(str_number):
    """
    :param str_number: str
    :return int
    """

    last = str_number[-1]
    result = 0

    for char in str_number:
        if char == last:
            result += int(char)
        last = char

    return result

# Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list.
# That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward
# matches it. Fortunately, your list has an even number of elements.


def second(str_number):
    """
    :param str_number: str
    :return int
    """

    list_number = list(str_number)
    total = list_number.__len__()
    half = total/2

    result = 0

    for key, x in enumerate(list_number):
        index_y = int((key + half) % total)

        if x == list_number[index_y]:
            result += int(x)

    return result


def test_first():
    assert first("1122") == 3
    assert first("1111") == 4
    assert first("1234") == 0
    assert first("91212129") == 9


def test_second():
    assert second("1212") == 6
    assert second("1221") == 0
    assert second("123425") == 4
    assert second("123123") == 12
    assert second("12131415") == 4


if __name__ == '__main__':
    test_first()
    test_second()

    with open("input_1.txt") as input_file:
        input_number = input_file.read()

    print(first(input_number))
    print(second(input_number))
