import re, sys, os, copy, dataclasses, time


TEST = False
def main():
    start_time = time.perf_counter()

    with open('test_input' if TEST else 'input', 'r') as f:
        input = f.readlines()
    print('input:')
    print(input)

    grid = []
    guard = None
    direction = 0
    for i in range(len(input)):
        grid.append(list(input[i].strip()))
        if "^" in input[i]:
            guard = (input[i].index("^"), i)
    print(grid)
    print(guard)
    print(direction)

    count = 0
    for i in range(len(grid[0])):
        print(count)
        for j in range(len(grid)):
            if grid[j][i] == '.':
                grid[j][i] = '#'
                if is_loop(grid, guard, direction):
                    count += 1
                grid[j][i] = '.'
    print(count)
    print("Took " + str(time.perf_counter() - start_time) + " seconds")



def is_loop(grid, guard, direction):
    visited = set()
    visited.add((guard, direction))
    while True:
        if direction == 0:
            next = (guard[0], guard[1] - 1)
        elif direction == 1:
            next = (guard[0] + 1, guard[1])
        elif direction == 2:
            next = (guard[0], guard[1] + 1)
        elif direction == 3:
            next = (guard[0] - 1, guard[1])
        else:
            raise Exception()

        if not is_on_grid(grid, next):
            return False
        elif is_occupied(grid, next):
            direction = (direction + 1) % 4
        elif (next, direction) in visited:
            return True
        else:
            visited.add((next, direction))
            guard = next


def is_on_grid(grid, coord):
    return 0 <= coord[0] < len(grid[0]) and 0 <= coord[1] < len(grid)

def is_occupied(grid, coord):
    return grid[coord[1]][coord[0]] == '#'

    #TODO

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
