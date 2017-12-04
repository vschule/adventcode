from collections import defaultdict



def isValid(input_line):
    words = input_line.split()
    words_set = set(words)

    if words.__len__() == words_set.__len__():
        return True
    return False

def first(str_input):
    lines = str_input.splitlines()

    count = sum(1 for line in lines if isValid(line))

    return count


def test_first():

    assert isValid('aa bb cc dd ee') == True
    assert isValid('aa bb cc dd aa') == False
    assert isValid('aa bb cc dd aaa') == True
    assert first('aa bb cc dd aaa\naa bb cc dd ee\naa bb cc dd aa') == 2


def isValid2(input_line):
    words = input_line.split()

    words_list = []
    for word in words:
        letters = list(word)
        letters.sort()
        letters = str(letters)
        words_list.append(letters)

    words_set = set(words_list)

    if words_list.__len__() == words_set.__len__():
        return True
    return False

def second(str_input):
    lines = str_input.splitlines()

    count = sum(1 for line in lines if isValid2(line))

    return count

def test_second():
    assert isValid2('abcde fghij') == True
    assert isValid2('abcde xyz ecdab') == False
    assert isValid2('a ab abc abd abf abj') == True
    assert isValid2('iiii oiii ooii oooi oooo') == True
    assert isValid2('oiii ioii iioi iiio') == False

    assert second('iiii oiii ooii oooi oooo\noiii ioii iioi iiio') == 1


if __name__ == '__main__':
    test_first()
    test_second()

    with open('input_4.txt', 'r') as input_file:
        input_value = input_file.read()

    print("first problem :", first(input_value))
    print("second problem:", second(input_value))


