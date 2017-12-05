from collections import defaultdict
import numpy as np


def first(str_input):
    lines = str_input.splitlines()
    wires = {}
    for line in lines:
        inputs, operation, output = parse(line)
        wires[output] = {'inputs': inputs, 'operation': operation}

    result = getresult(wires, 'a')
    return result

def getresult(wires, letter):
    try :
        wire = wires[letter]
    except KeyError:
        return letter

    if wire.get('results'):
        return wire['results']

    values = []
    for input in wire['inputs']:
        values.append(getresult(wires, input))

    result = wire['operation'](values)
    wire['results'] = result
    return result


def parse(statement):
    inputs = []

    tokens, output = statement.split(' -> ')

    operations = {'AND': andgate, 'OR': orgate, 'LSHIFT': lshift, 'RSHIFT': rshift, 'NOT': notgate}
    operation = provide

    for token in tokens.split():

        if token.isnumeric():
            inputs.append(np.uint16(token))

        elif token in operations:
            operation = operations[token]

        else:
            inputs.append(token)

    return inputs, operation, output


def provide(value):
    return value[0]


def andgate(values):
    return values[0] & values[1]

def notgate(value1):
    value = (1 << 16) - 1 - value1[0]
    return value

def orgate(value1):
    return value1[0] | value1[1]


def lshift(value1):
    return value1[0] << value1[1]


def rshift(value1):
    return value1[0] >> value1[1]


def run(str_input):
    return


def test_first():
    first_col = '123 -> x\n' \
                '456 -> y\n' \
                'x AND y -> d\n' \
                'x OR y -> e\n' \
                'x LSHIFT 2 -> f\n' \
                'y RSHIFT 2 -> g  \n' \
                'NOT x -> h\n' \
                'NOT y -> i\n' \
                'y -> a'

    first_answer = {'d': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456}

    assert first(first_col) == 456


def second(str_input):
    lines = str_input.splitlines()
    wires = {}
    for line in lines:
        inputs, operation, output = parse(line)
        wires[output] = {'inputs': inputs, 'operation': operation}

    result = getresult(wires, 'a')
    for wire in wires:
        if wires[wire].get('results'):
            wires[wire].pop('results')

    wires['b']['results'] = result
    return getresult(wires, 'a')



def test_second():
    return
    assert second('turn on 0,0 through 0,0') == 1
    assert second('toggle 0,0 through 999,999') == 2000000


if __name__ == '__main__':
    test_first()
    test_second()

    with open('input_7.txt', 'r') as input_file:
        input_value = input_file.read()

    print("first problem :", first(input_value))
    print("second problem:", second(input_value))
