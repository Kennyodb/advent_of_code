import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    result = 0
    for line in input:
        digits = [0 for _ in range(12)]
        for ci, c in enumerate(line):
            n = int(c)
            for di, d in enumerate(digits):
                if n > d and len(line) - ci >= len(digits) - di:
                    digits[di] = n
                    for i in range(di+1, len(digits)):
                        digits[i] = 0
                    break
        highest = int(''.join([str(d) for d in digits]))
        print(highest)
        result += highest
    print(result)



    print("Took " + str(time.perf_counter() - start_time) + " seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
