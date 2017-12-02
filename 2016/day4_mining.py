# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.
# The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal.
# To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...)
#  that produces such a hash.

import hashlib


class md5_start:
    """ Iterator that breaks when 00000 is found at the start of an md5 hash """

    def __init__(self, secretkey, start_string):
        self.secretkey = secretkey
        self.start_string = start_string

    def __iter__(self):
        self.iteration = 0
        return self

    def __next__(self):
        result = self.secretkey + str(self.iteration)
        hash_result = hashlib.md5(bytes(result, 'utf8')).hexdigest()

        if hash_result.startswith(self.start_string):
            raise StopIteration

        self.iteration += 1
        return self.iteration


def first(str_input):
    last = 0
    for x in md5_start(str_input, '00000'):
        last = x

    return last


# Now with 6 zeroes
def second(str_input):
    last = 0
    for x in md5_start(str_input, '000000'):
        last = x

    return last


def test_first():
    assert first('abcdef') == 609043
    assert first('pqrstuv') == 1048970


def test_second():
    return


if __name__ == '__main__':
    test_first()
    test_second()

    input_value = "yzbqklnj"

    print(first(input_value))
    print(second(input_value))
