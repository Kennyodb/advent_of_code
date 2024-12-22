import re, sys, os, copy, dataclasses, time, math


TEST = False

def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    i = 0
    robot_x = -1
    robot_y = -1
    grid = []
    while len(input[i]) > 0:
        l = list(input[i])
        if '@' in l:
            robot_y = i
            robot_x = l.index('@')
            l[robot_x] = '.'
        grid.append(l)
        i += 1

    cmd_list = []
    i += 1
    while i < len(input):
        cmd_list.extend(list(input[i]))
        i += 1

    new_grid = []
    for line in grid:
        new_line = []
        for e in line:
            if e == '#':
                new_line.append('#')
                new_line.append('#')
            elif e == '.':
                new_line.append('.')
                new_line.append('.')
            elif e == 'O':
                new_line.append('[')
                new_line.append(']')
        new_grid.append(new_line)
    grid = new_grid
    robot_x = robot_x * 2

    print_grid(grid)
    print(robot_x)
    print(robot_y)
    print(cmd_list)

    for cmd in cmd_list:
        # print(cmd)
        boxes_to_move = find_boxes_to_move(grid, robot_x, robot_y, cmd)
        if boxes_to_move is None:
            continue
        robot_x, robot_y = get_neighbour(robot_x, robot_y, cmd)
        if len(boxes_to_move) > 0:
            new_grid = copy.deepcopy(grid)
            for coord in boxes_to_move:
                new_grid[coord[1]][coord[0]] = '.'
            for coord in boxes_to_move:
                new_coord = get_neighbour(coord[0], coord[1], cmd)
                new_grid[new_coord[1]][new_coord[0]] = grid[coord[1]][coord[0]]
            grid = new_grid
        # print_grid_and_robot(grid, robot_x, robot_y)

    print_grid_and_robot(grid, robot_x, robot_y)

    gps_sum = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if is_box_left(grid, x, y):
                gps_sum += 100 * y + x
    print(gps_sum)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def print_grid(grid):
    for line in grid:
        print("".join(line))


def print_grid_and_robot(grid, robot_x, robot_y):
    grid = copy.deepcopy(grid)
    grid[robot_y][robot_x] = '@'
    print_grid(grid)


# [(x, y)...] -> can move, and these boxes are pushed
# None -> cannot move
def find_boxes_to_move(grid, x, y, direction):
    x, y = get_neighbour(x, y, direction)
    if is_free(grid, x, y):
        return set()
    if is_wall(grid, x, y):
        return None

    boxes = {(x, y)}
    next_boxes = find_boxes_to_move(grid, x, y, direction)
    if next_boxes is None:
        return None
    boxes.update(next_boxes)

    if not is_horizontal(direction):
        other_x = x+1 if is_box_left(grid, x, y) else x-1
        boxes.add((other_x, y))
        other_next_boxes = find_boxes_to_move(grid, other_x, y, direction)
        if other_next_boxes is None:
            return None
        boxes.update(other_next_boxes)

    return boxes

def find_free(grid, x, y, direction):
    x, y = get_neighbour(x, y, direction)
    while is_on_grid(grid, x, y):
        if is_free(grid, x, y):
            return x, y
        if is_wall(grid, x, y):
            break
        x, y = get_neighbour(x, y, direction)
    return None


def is_horizontal(direction):
    return direction == '<' or direction == '>'


def get_neighbour(x, y, direction):
    if direction == '^':
        return x, y - 1
    if direction == 'v':
        return x, y + 1
    if direction == '<':
        return x - 1, y
    if direction == '>':
        return x + 1, y


def is_wall(grid, x, y):
    return grid[y][x] == '#'


def is_free(grid, x, y):
    return grid[y][x] == '.'


def is_box(grid, x, y):
    return grid[y][x] == '[' or grid[y][x] == ']'


def is_box_left(grid, x, y):
    return grid[y][x] == '['


def is_on_grid(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
