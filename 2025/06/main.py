import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    # rows = []
    # for line in input:
    #     line = re.sub(' +', ' ', line).strip()
    #     print(line)
    #     if line.startswith('*') or line.startswith('+'):
    #         ops = line.split(' ')

    ops_line = input.pop(len(input) - 1)
    ops = re.sub(' +', ' ', ops_line.strip()).split(' ')
    all_numbers = []
    current_numbers = []
    for i in range(len(input[0])):
        digits = [r[i] for r in input]
        if all([d == ' ' for d in digits]):
            all_numbers.append(current_numbers)
            current_numbers = []
        else:
            number = 0
            for d in digits:
                if d != ' ':
                    number *= 10
                    number += int(d)
            current_numbers.append(number)
    all_numbers.append(current_numbers)


    print(all_numbers)
    print(ops)

    result = 0
    for i in range(len(ops)):
        subresult = all_numbers[i][0]
        op = ops[i]
        for j in range(1, len(all_numbers[i])):
            if op == '*':
                subresult *= all_numbers[i][j]
            else:
                subresult += all_numbers[i][j]
        result += subresult
    print(result)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
