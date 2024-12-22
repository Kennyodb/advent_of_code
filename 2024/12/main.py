import re, sys, os, copy, dataclasses, time, math


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    groups = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if in_any_group(groups, (j, i)):
                continue
            group = set()
            add_to_group(input, j, i, input[i][j], group)
            groups.append(group)

    print(groups)
    print(len(groups))

    total = 0
    for group in groups:
        area = len(group)
        # perimeter = get_perimeter(group)
        # cost = area * perimeter
        sides = get_nb_sides(group)
        cost = area * sides
        print(cost)
        total += cost
    print(total)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def add_to_group(grid, x, y, char, group):
    if not is_on_grid(grid, x, y):
        return
    if grid[y][x] != char:
        return
    if (x,y) in group:
        return

    group.add((x,y))
    add_to_group(grid, x - 1, y, char, group)
    add_to_group(grid, x + 1, y, char, group)
    add_to_group(grid, x, y - 1, char, group)
    add_to_group(grid, x, y + 1, char, group)


def get_perimeter(group):
    perimeter = 0
    for coord in group:
        if (coord[0] - 1, coord[1]) not in group:
            perimeter += 1
        if (coord[0] + 1, coord[1]) not in group:
            perimeter += 1
        if (coord[0], coord[1] - 1) not in group:
            perimeter += 1
        if (coord[0], coord[1] + 1) not in group:
            perimeter += 1
    return perimeter

def get_nb_sides(group):
    sides = 0
    for coord in group:
        if (coord[0] - 1, coord[1]) not in group:
            if not (((coord[0], coord[1] - 1) in group) and not ((coord[0] - 1, coord[1] - 1) in group)):
                sides += 1
        if (coord[0] + 1, coord[1]) not in group:
            if not (((coord[0], coord[1] - 1) in group) and not ((coord[0] + 1, coord[1] - 1) in group)):
                sides += 1
        if (coord[0], coord[1] - 1) not in group:
            if not (((coord[0] - 1, coord[1]) in group) and not ((coord[0] - 1, coord[1] - 1) in group)):
                sides += 1
        if (coord[0], coord[1] + 1) not in group:
            if not (((coord[0] - 1, coord[1]) in group) and not ((coord[0] - 1, coord[1] + 1) in group)):
                sides += 1
    return sides

def is_on_grid(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def in_any_group(groups, coord):
    for group in groups:
        if coord in group:
            return True
    return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
