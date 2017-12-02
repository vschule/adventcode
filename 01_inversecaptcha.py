import day1_inversecaptcha

def solution(str_number):
    z = 0

    result = 0

    for x in str_number:
        if x == z:
            result += int(x)
        z = x

    return result


if __name__ == '__main__':
    with open("input.txt") as input_file:
        input_number = input_file.read()


    number = input_number + input_number[0]

    print(solution(number))
