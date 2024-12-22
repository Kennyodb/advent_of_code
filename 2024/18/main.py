import re, sys, os, copy, dataclasses, time, math
from collections import deque


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    bytes = [(int(s.split(",")[0]), int(s.split(",")[1])) for s in input]

    width = 7 if TEST else 71
    height = 7 if TEST else 71

    grid = [['.'] * width for _ in range(height)]

    for i in range(len(bytes)):
        print(i)
        b = bytes[i]
        grid[b[1]][b[0]] = '#'
        dist, prev = dijkstra(grid, (0, 0))
        if dist.get((width-1, height-1)) is None:
            print(b)
            break

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def dijkstra(grid, start_node):
    dist = {start_node: 0}
    prev = {start_node: []}
    queue = deque([start_node])

    while len(queue) > 0:
        node = queue.popleft()
        val = dist.get(node)

        for next_node in [above(node), below(node), left_of(node), right_of(node)]:
            if is_on_grid(grid, next_node) and not is_corrupted(grid, next_node):
                prev_val = dist.get(next_node)
                if prev_val is None or prev_val > val + 1:
                    dist[next_node] = val + 1
                    prev[next_node] = [node]
                    queue.append(next_node)
                elif val + 1 == prev_val:
                    prev[next_node].append(node)

    return dist, prev


def above(node):
    return node[0], node[1] - 1

def right_of(node):
    return node[0] + 1, node[1]

def below(node):
    return node[0], node[1] + 1

def left_of(node):
    return node[0] - 1, node[1]


def is_corrupted(grid, node):
    return grid[node[1]][node[0]] == '#'


def is_on_grid(grid, coord):
    return 0 <= coord[0] < len(grid[0]) and 0 <= coord[1] < len(grid)


def print_grid(grid):
    for line in grid:
        print("".join(line))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
