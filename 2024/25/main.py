import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    locks = []
    keys = []

    i = 0
    while i < len(input):
        arr = [0] * 5
        for j in range(5):
            line = input[i + j + 1]
            for k in range(len(line)):
                if line[k] == '#':
                    arr[k] += 1
        if input[i] == "#####":
            locks.append(arr)
        else:
            keys.append(arr)
        i += 8

    print(locks)
    print(keys)

    total = 0
    for lock in locks:
        for key in keys:
            if max([lock[i] + key[i] for i in range(len(lock))]) <= 5:
                total += 1
    print(total)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
