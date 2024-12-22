import re, sys, os, copy, dataclasses


TEST = False
def main():
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.readlines()
    print('input:')
    print(input)

    numbers = []
    for line in input:
        split = line.strip().split(" ")
        arr = [int(split[0][0:-1])]
        for i in range(1, len(split)):
            arr.append(int(split[i]))
        numbers.append(arr)
    print(numbers)

    pt1_result = 0
    for arr in numbers:
        if is_solvable(arr[0], arr[1:]):
            pt1_result += arr[0]
    print(pt1_result)


def is_solvable(result, factors):
    return accumulate(result, factors[0], factors[1:], ['+', '*', '||'])


def accumulate(target, result, remaining_factors, operators):
    if len(remaining_factors) == 0:
        return result == target

    for op in operators:
        if op == '+':
            next_result = result + remaining_factors[0]
        elif op == '*':
            next_result = result * remaining_factors[0]
        elif op == '||':
            next_result = result
            for i in range(len(str(remaining_factors[0]))):
                next_result *= 10
            next_result += remaining_factors[0]
        else:
            raise Exception("aah")
        if accumulate(target, next_result, remaining_factors[1:], operators):
            return True
    return False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
