from collections import defaultdict
import numpy as np


def first(str_input, code_input):
    lines = str_input.splitlines()
    literal_count = 0
    for line in lines:
        literal_count += line.__len__()

    lines = code_input.splitlines()
    code_count = sum(line.__len__() for line in lines)

    return literal_count -code_count




def test_first():
    return
    assert first('"\x27"') == 5

    assert first('""') == 2
    assert first('"abc"') == 3
    assert first('"aaa\"aaa"') == 3
    assert first('"abc"\n"\x27"') == 8




def second(str_input):
    return



def test_second():
    return
    assert second('turn on 0,0 through 0,0') == 1
    assert second('toggle 0,0 through 999,999') == 2000000


if __name__ == '__main__':
    with open('input_8.txt', 'r') as input_file:
        litteral_value = input_file.read()

    import codecs
    with codecs.open('input_8.txt', 'r', encoding='unicode_escape') as input_file:
        code_value = input_file.read()

    print("first problem :", first(litteral_value, code_value))
    print("second problem:", second('x'))
