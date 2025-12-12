import re, sys, os, copy, dataclasses, time, math, itertools, collections
from os.path import pathsep

TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    nodes = dict()
    for line in input:
        split = line.split(' ')
        nodes[split[0][0:-1]] = (split[1:])
    nodes['out'] = []

    reverse_nodes = dict()
    for key in nodes:
        reverse_nodes[key] = []
    for node in nodes.items():
        for next_node in node[1]:
            reverse_nodes[next_node].append(node[0])

    svr2fft = count_paths('svr', 'fft', nodes, reverse_nodes)
    print(svr2fft)
    fft2dac = count_paths('fft', 'dac', nodes, reverse_nodes)
    print(fft2dac)
    dac2out = count_paths('dac', 'out', nodes, reverse_nodes)
    print(dac2out)

    print(svr2fft * fft2dac * dac2out)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def count_paths(start, target, nodes, reverse_nodes):
    count = 0
    queue = collections.deque([target])
    reachable_nodes = get_reachable_nodes(start, nodes)
    while len(queue) > 0:
        node = queue.popleft()
        for next_node in reverse_nodes[node]:
            if next_node == start:
                count += 1
            elif next_node in reachable_nodes:
                queue.append(next_node)
    return count


def get_reachable_nodes(start, nodes):
    reachable = {start}
    queue = collections.deque([start])
    while len(queue) > 0:
        node = queue.popleft()
        for next_node in nodes[node]:
            if not next_node in reachable:
                reachable.add(next_node)
                queue.append(next_node)
    return reachable


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
