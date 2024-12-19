import re, sys, os, copy, dataclasses, time, math, itertools

TEST = False

def main():
    start_time = time.perf_counter()
    with open('test_input' if TEST else 'input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    towels = input[0].split(", ")
    patterns = input[2:]

    total = 0
    for pattern in patterns:
        counts_by_pattern = {"": 1}
        for i in range(1, len(pattern)):
            end = pattern[-i:]
            counts_by_pattern[end] = count_breakdowns(end, towels, counts_by_pattern)
        count = count_breakdowns(pattern, towels, counts_by_pattern)
        print(count)
        total += count
    print(total)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def count_breakdowns(pattern, towels, counts_by_pattern):
    total = 0
    for towel in towels:
        if pattern.startswith(towel):
            total += counts_by_pattern.get(pattern[len(towel):])
    return total


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
