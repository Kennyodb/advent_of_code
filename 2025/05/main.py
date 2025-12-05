import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    ranges = []

    i = 0
    while len(input[i]) > 0:
        split = input[i].split('-')
        ranges.append((int(split[0]), int(split[1])))
        i += 1

    result = 0
    for j in range(i+1, len(input)):
        if is_in_any_range(int(input[j]), ranges):
            result += 1
    print(result)

    collapsed_ranges = collapse_all(ranges)
    result2 = 0
    for r in collapsed_ranges:
        print(r)
        result2 += r[1] + 1 - r[0]
    print(result2)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def collapse_all(ranges):
    while True:
        new_ranges = collapse_once(ranges)
        if len(new_ranges) == len(ranges):
            return ranges
        ranges = new_ranges


def collapse_once(ranges):
    new_ranges = []
    for i in range(len(ranges)):
        for j in range(i+1, len(ranges)):
            collapsed = try_collapse(ranges[i], ranges[j])
            if collapsed is not None:
                new_ranges.append(collapsed)
                for k in range(i+1, len(ranges)):
                    if k != j:
                        new_ranges.append(ranges[k])
                return new_ranges
        new_ranges.append(ranges[i])
    return new_ranges


def try_collapse(r1, r2):
    if is_in_range(r1[0], r2) or is_in_range(r1[1], r2) or is_in_range(r2[0], r1) or is_in_range(r2[1], r1):
        return min(r1[0], r2[0]), max(r1[1], r2[1])
    return None


def is_in_any_range(number, ranges):
    for r in ranges:
        if is_in_range(number, r):
            return True
    return False


def is_in_range(number, r):
    return r[0] <= number <= r[1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
