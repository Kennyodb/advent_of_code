import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    dial = 50
    zeroes = 0
    for line in input:
        length = int(line[1:])
        while length > 100:
            zeroes += 1
            length -= 100
        if line[0] == 'L':
            if 0 < dial <= length:
                zeroes += 1
            dial = (dial - length + 100) % 100
        else:
            if 0 < dial and dial + length >= 100:
                zeroes += 1
            dial = (dial + length) % 100
    print('zeroes:', zeroes)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
