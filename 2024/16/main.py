import re, sys, os, copy, dataclasses, time, math
from collections import deque


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    start_node = (1, len(input) - 2, 1)  # x, y, dir
    # 0 - North; 1 - East; 2 - South; 3 - West

    end_x = len(input[0]) - 2
    end_y = 1

    dist, prev = dijkstra(input, start_node)

    fastest = min(dist[(end_x, end_y, 0)], dist[(end_x, end_y, 1)])
    print(fastest)

    queue = deque([])
    end_node = (end_x, end_y, 0)
    alt_end_node = (end_x, end_y, 1)
    if dist.get(end_node) < dist.get(alt_end_node):
        queue.append(end_node)
    elif dist.get(end_node) < dist.get(alt_end_node):
        queue.append(alt_end_node)
    else:
        queue.append(end_node)
        queue.append(alt_end_node)

    best_seats = set()
    while len(queue) > 0:
        node = queue.popleft()
        best_seats.add((node[0], node[1]))
        queue.extend(prev.get(node))

    print(len(best_seats))

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def dijkstra(grid, start_node):
    dist = {start_node: 0}
    prev = {start_node: []}
    queue = deque([start_node])

    while len(queue) > 0:
        node = queue.popleft()
        val = dist.get(node)

        fwd = get_forward_node(node)
        if not is_wall(grid, fwd):
            fwd_val = dist.get(fwd)
            new_fwd_val = val + 1
            if fwd_val is None or new_fwd_val < fwd_val:
                dist[fwd] = new_fwd_val
                prev[fwd] = [node]
                queue.append(fwd)
            elif new_fwd_val == fwd_val:
                prev[fwd].append(node)

        left = get_turn_left_node(node)
        left_val = dist.get(left)
        new_left_val = val + 1000
        if left_val is None or new_left_val < left_val:
            dist[left] = new_left_val
            prev[left] = [node]
            queue.append(left)
        elif new_left_val == left_val:
            prev[left].append(node)

        right = get_turn_right_node(node)
        right_val = dist.get(right)
        new_right_val = val + 1000
        if right_val is None or new_right_val < right_val:
            dist[right] = new_right_val
            prev[right] = [node]
            queue.append(right)
        elif new_right_val == right_val:
            prev[right].append(node)

    return dist, prev


def get_forward_node(node):
    if node[2] == 0:
        return node[0], node[1] - 1, node[2]
    elif node[2] == 1:
        return node[0] + 1, node[1], node[2]
    elif node[2] == 2:
        return node[0], node[1] + 1, node[2]
    else:
        return node[0] - 1, node[1], node[2]


def get_turn_left_node(node):
    return node[0], node[1], (node[2] + 3) % 4


def get_turn_right_node(node):
    return node[0], node[1], (node[2] + 1) % 4


def is_wall(grid, node):
    return grid[node[1]][node[0]] == '#'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
