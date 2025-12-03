import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    result = 0
    for span in input[0].split(','):
        start = int(span.split('-')[0])
        end = int(span.split('-')[1])
        for n in range(start, end+1):
            if is_invalid(n):
                print('invalid: ' + str(n))
                result += n

    print('result:' + str(result))

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def is_invalid(n):
    string = str(n)
    for seq_length in range(1, int(len(string) / 2) + 1):
        if is_repeating(string, seq_length):
            return True
    return False

    # mid = int(len(string) / 2)
    # return string[:mid] == string[mid:]

def is_repeating(string, seq_length):
    if len(string) % seq_length != 0:
        return False
    seq = string[:seq_length]
    for i in range(0, len(string), seq_length):
        if string[i:i+seq_length] != seq:
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    is_invalid(38593859)
    main()
