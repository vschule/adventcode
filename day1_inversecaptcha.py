
if __name__ == '__main__':
    with open("input.txt") as input_file:
        input_number = input_file.read()

    list_number = list(input_number)

    total = list_number.__len__()
    half = total / 2

    result = 0

    for key, x in enumerate(list_number):
        index_y = int((key + half)%total)

        if x == list_number[index_y]:
            result += int(x)

    print(result)
