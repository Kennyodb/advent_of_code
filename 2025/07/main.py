import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    splits = 0
    beams =  [dict() for _ in range(len(input))]
    beams[0][input[0].index('S')] = 1
    for i in range(1, len(input)):
        line = input[i]
        for beam, count in beams[i-1].items():
            if line[beam] == '.':
                beams[i][beam] = beams[i].get(beam, 0) + count
            else:
                beams[i][beam-1] = beams[i].get(beam-1, 0) + count
                beams[i][beam+1] = beams[i].get(beam+1, 0) + count
                splits += 1
    print(beams[-1])
    for b in beams:
        print(b.values())
    print(sum(beams[-1].values()))

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
