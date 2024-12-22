import re, sys, os, copy, dataclasses, time, math, itertools
from collections import deque


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    start = None
    end = None
    for i in range(len(input)):
        s = input[i].find("S")
        if s > 0:
            start = (s, i)
        e = input[i].find("E")
        if e > 0:
            end = (e, i)
    print(start)
    print(end)

    dist, trace = dijkstra(input, end)
    cheats = find_cheats(input, start, dist, trace)

    cheats.sort(key=lambda c: c[2])
    cheats_by_time_saved = {}
    for cheat in cheats:
        cheats_by_time_saved.setdefault(cheat[2], []).append(cheat)

    total = 0
    for entry in cheats_by_time_saved.items():
        if entry[0] < 100:
            continue
        nb_cheats = len(entry[1])
        total += nb_cheats
        print(str(entry[0]) + ": " + str(nb_cheats))
    print(total)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def find_cheats(grid, start_node, dist, trace):
    cheats = []
    queue = deque([start_node])
    while len(queue) > 0:
        node = queue.popleft()
        cheats.extend(find_cheats_that_end_at(grid, node, 20, dist))
        queue.extend(trace.get(node))
    return cheats


def find_cheats_that_end_at(grid, cheat_end, max_cheat_dist, dist):
    cheats = []
    cheat_end_val = dist.get(cheat_end)

    x_min = max(cheat_end[0] - max_cheat_dist, 0)
    y_min = max(cheat_end[1] - max_cheat_dist, 0)
    x_max = min(cheat_end[0] + max_cheat_dist + 1, len(grid[0]))
    y_max = min(cheat_end[1] + max_cheat_dist + 1, len(grid))

    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            node = (x, y)
            cheat_dist = manhattan(node, cheat_end)
            if cheat_dist <= max_cheat_dist and not is_wall(grid, node):
                val = dist.get(node)
                if val is not None and val + cheat_dist < cheat_end_val:
                    time_saved = cheat_end_val - val - cheat_dist
                    cheats.append((node, cheat_end, time_saved))

    return cheats


def dijkstra(grid, start_node):
    dist = {start_node: 0}
    prev = {start_node: []}
    queue = deque([start_node])

    while len(queue) > 0:
        node = queue.popleft()
        val = dist.get(node)

        for next_node in [above(node), below(node), left_of(node), right_of(node)]:
            if is_on_grid(grid, next_node) and not is_wall(grid, next_node):
                prev_val = dist.get(next_node)
                if prev_val is None or prev_val > val + 1:
                    dist[next_node] = val + 1
                    prev[next_node] = [node]
                    queue.append(next_node)
                elif val + 1 == prev_val:
                    prev[next_node].append(node)

    return dist, prev


def manhattan(n1, n2):
    return abs(n2[0] - n1[0]) + abs(n2[1] - n1[1])


def above(node):
    return node[0], node[1] - 1


def right_of(node):
    return node[0] + 1, node[1]


def below(node):
    return node[0], node[1] + 1


def left_of(node):
    return node[0] - 1, node[1]


def is_wall(grid, node):
    return grid[node[1]][node[0]] == '#'


def is_on_grid(grid, coord):
    return 0 <= coord[0] < len(grid[0]) and 0 <= coord[1] < len(grid)


def print_grid(grid):
    for line in grid:
        print("".join(line))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
