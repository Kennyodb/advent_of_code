import re, sys, os, copy, dataclasses, time, math


TEST = True
def main():
    start_time = time.perf_counter()
    with open('test_input' if TEST else 'input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    #TODO

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
