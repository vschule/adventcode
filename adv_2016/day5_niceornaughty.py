
def first(str_input):
    count = 0
    for line in str_input.splitlines():
        if isNice(line):
            count += 1

    return count




# A nice string is one with all of the following properties:
#    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
FORBIDDEN = ['ab', 'cd', 'pq', 'xy']
VOWELS = ['a', 'e', 'i', 'o', 'u']

def isNice(str_input):

    count = 0
    repetition = False
    last = ''

    for char in str_input:
        if char in VOWELS:
            count += 1

        if char == last:
            repetition = True
        last = char

    if any(xs in str_input for xs in FORBIDDEN):
        return False

    return count >= 3 and repetition

def test_first():
    assert isNice('ugknbfddgicrmopn') == True
    assert isNice('aaa') == True
    assert isNice('jchzalrnumimnmhp') == False
    assert isNice('haegwjzuvuyypxyu') == False
    assert isNice('dvszwmarrgswjxmb') == False

    assert first('jchzalrnumimnmhp\nhaegwjzuvuyypxyu\ndvszwmarrgswjxmb\naaa') == 1
    assert first('ugknbfddgicrmopn\nhaegwjzuvuyypxyu\ndvszwmarrgswjxmb\naaa') == 2


# Now, a nice string is one with all of the following properties:
# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy)
#  or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx,
#  abcdefeghi (efe), or even aaa.


def second(str_input):
    count = 0
    for line in str_input.splitlines():
        if isNice2(line):
            count += 1

    return count


def isNice2(str_input):
    maximum = str_input.__len__()
    i = 2

    bin_condition = False
    repeat = False

    while i < maximum:
        binome = str_input[i-2:i]
        rest = str_input[i:]

        if binome in rest:
            bin_condition = True

        if str_input[i] == str_input[i-2]:
            repeat = True
        i += 1

    return repeat and bin_condition


def test_second():
    assert isNice2('qjhvhtzxzqqjkmpb') == True
    assert isNice2('xxyxx') == True
    assert isNice2('uurcxstgmygtbstg') == False
    assert isNice2('ieodomkazucvgmuy') == False
    assert second('ieodomkazucvgmuy\nqjhvhtzxzqqjkmpb\nqjhvhtzxzqqjkmpb\nxxyxx') == 3


if __name__ == '__main__':
    test_first()
    test_second()

    with open('input_5.txt', 'r') as input_file:
        input_value = input_file.read()

    print("first problem :", first(input_value))
    print("second problem:", second(input_value))
