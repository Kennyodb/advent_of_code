import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    global input, width, height
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    height = len(input)
    width = len(input[0])

    initial_count = count_all()

    current_count = initial_count
    while True:
        for y in range(height):
            for x in range(width):
                if input[y][x] == '@':
                    neighbours = count_neighbours(x, y)
                    if neighbours < 4:
                        input[y] = input[y][0:x] + '.' + input[y][x+1:width]
        next_count = count_all()
        if next_count == current_count:
            break
        current_count = next_count

    print(initial_count - current_count)


    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def count_all():
    count = 0
    for line in input:
        count += line.count('@')
    return count

def count_neighbours(x, y):
    min_x = max(0, x - 1)
    min_y = max(0, y - 1)
    max_x = min(x + 1, width - 1)
    max_y = min(y + 1, height - 1)
    count = 0
    for nx in range(min_x, max_x + 1):
        for ny in range(min_y, max_y + 1):
            if nx == x and ny == y:
                continue
            if input[ny][nx] == '@':
                count += 1
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
