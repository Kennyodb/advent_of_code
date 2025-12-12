import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    shapes = [set(), set(), set(), set(), set(), set()] # 6 shapes
    for shape_i in range(len(shapes)):
        offset = shape_i * 5 + 1
        for i in range(3):
            line = input[offset + i]
            for j in range(len(line)):
                if line[j] == '#':
                    shapes[shape_i].add((j,i))
    print(shapes)

    all_regions = []
    for line in input[30:]:
        split = line.replace(':', '').split(' ')
        width = int(split[0].split('x')[0])
        height = int(split[0].split('x')[1])
        presents = [int(n) for n in split[1:]]
        all_regions.append((width, height, presents))

    impossible = []
    possible = []
    maybe = []

    for width, height, presents in all_regions:
        required_space = 0
        for i in range(len(presents)):
            shape = shapes[i]
            count = presents[i]
            size = len(shape)
            required_space += size * count
        slots3by3 = int(width / 3) * int(height / 3)
        total_presents = sum(presents)
        if slots3by3 >= total_presents:
            possible.append((width, height, presents))
        elif required_space > width * height:
            impossible.append((width, height, presents))
        else:
            maybe.append((width, height, presents))

    print(str(len(possible)) + ' definitely possible.')
    print(str(len(impossible)) + ' definitely impossible.')
    print(str(len(maybe)) + '  maybe.')


    print("Took " + str(time.perf_counter() - start_time) + " seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
