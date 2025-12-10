import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    tiles = []
    for line in input:
        split = line.split(',')
        tiles.append((int(split[0]), int(split[1])))

    largest_square = None
    largest_size = 0
    for i in range(len(tiles)):
        t1 = tiles[i]
        for j in range(i+1, len(tiles)):
            t2 = tiles[j]
            min_x = min(t1[0], t2[0])
            min_y = min(t1[1], t2[1])
            max_x = max(t1[0], t2[0])
            max_y = max(t1[1], t2[1])
            size = (max_x - min_x + 1) * (max_y - min_y + 1)
            if size > largest_size:
                valid = True
                for k in range(len(tiles)):
                    if k == i or k == j:
                        continue
                    if is_strictly_inside(tiles[k], min_x, min_y, max_x, max_y) \
                            or edges_inwards(tiles[k], tiles[k-1], tiles[(k+1) % len(tiles)], min_x, min_y, max_x, max_y):
                        valid = False
                        break
                if valid:
                    largest_size = size
                    largest_square = (min_x, min_y, max_x, max_y)
    print(largest_size)
    print(largest_square)

    # 4616586187 too high

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def is_strictly_inside(tile, min_x, min_y, max_x, max_y):
    return min_x < tile[0] < max_x and min_y < tile[1] < max_y


def edges_inwards(tile, prev, next, min_x, min_y, max_x, max_y):
    # left
    if tile[0] <= min_x and min_y < tile[1] < max_y and (prev[0] > min_x or next[0] > min_x):
        return True
    # right
    if tile[0] >= max_x and min_y < tile[1] < max_y and (prev[0] < max_x or next[0] < max_x):
        return True
    # top
    if tile[1] <= min_y and min_x < tile[0] < max_x and (prev[1] > min_y or next[1] > min_y):
        return True
    # bottom
    if tile[1] >= max_y and min_x < tile[0] < max_x and (prev[1] < max_y or next[1] < max_y):
        return True

    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
