import re, sys, os, copy, dataclasses, time, math


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    a = int(input[0][12:])
    b = int(input[1][12:])
    c = int(input[2][12:])
    program = [int(e) for e in input[4][9:].split(",")]
    print(program)

    '''
    2,4, b = a % 8
    1,7, b = b xor 0111
    7,5, c = a / 2^b
    1,7, b = b xor 0111
    0,3, a = a / 8
    4,1, b = b xor c
    5,5, print b
    3,0  goto 0 unless a == 0
    
    b = last 3 bits of a
    c = a >> 7-b
    print b xor c mod 8
    a = a >> 3 and repeat
    '''

    # out = run(program, a, b, c)
    # print(out)

    combinations = {
        0: ['111'], # for b == 8, only this solution
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: []
    }
    for b in range(7):
        free = 7-b
        for i in range(pow(2, free)):
            s = bin(i)[2:].zfill(free) + bin(b)[2:].zfill(3)
            c = int(s, 2) >> free
            combinations[c ^ b].append(s)

    for i in range(8):
        combinations[i].sort(key=len)
        print(str(i) + ": " + str(combinations[i]))

    solutions = solve(program, combinations, "", 0)
    solutions_int = [int(s, 2) for s in solutions]
    solutions_int.sort()

    for s in solutions_int:
        out = run(program, s, b, c)
        if out == program:
            print(s)
            print(bin(s))

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def solve(program, combinations, ends_with, iteration):
    if len(program) == 0:
        return [ends_with]
    op = program[0]
    solutions = []
    must_end_at = len(ends_with) - (iteration * 3)
    for option in combinations.get(op):
        if len(option) <= must_end_at:
            if option != ends_with[must_end_at-len(option):must_end_at]:
                continue
        elif option[len(option)-must_end_at:] != ends_with[0:must_end_at]:
            continue
        s = option + ends_with[must_end_at:]
        sol = solve(program[1:], combinations, s, iteration + 1)
        len(s) - must_end_at - 3
        if sol is not None:
            solutions.extend(sol)
    return solutions


def run(program, a, b, c):
    ctr = 0
    out = []
    while ctr < len(program):
        operand = program[ctr + 1]
        if program[ctr] == 0:
            a = int(a / pow(2, combo(operand, a, b, c)))
        elif program[ctr] == 1:
            b = b ^ operand
        elif program[ctr] == 2:
            b = combo(operand, a, b, c) % 8
        elif program[ctr] == 3:
            if a != 0:
                ctr = operand
                continue
        elif program[ctr] == 4:
            b = b ^ c
        elif program[ctr] == 5:
            out.append(combo(operand, a, b, c) % 8)
        elif program[ctr] == 6:
            b = int(a / pow(2, combo(operand, a, b, c)))
        elif program[ctr] == 7:
            c = int(a / pow(2, combo(operand, a, b, c)))
        else:
            raise Exception()
        ctr += 2
    return out


def combo(operand, a, b, c):
    if operand < 4:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    raise Exception()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
