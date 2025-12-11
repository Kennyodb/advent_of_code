import re, sys, os, copy, dataclasses, time, math, itertools, collections
from os.path import pathsep

TEST = True
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

    result = 0
    paths = count_paths('svr', 'out', nodes, reverse_nodes)
    print(paths)

    print(result)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def count_paths(start, target, nodes, reverse_nodes):
    count = 0
    paths_to_target = dict([(target,1)])
    queue = collections.deque([target])

    reachable_nodes = get_reachable_nodes(start, nodes)

    while len(queue) > 0:
        next_queue = collections.deque()
        next_paths_to_target = copy.deepcopy(paths_to_target)
        while len(queue) > 0:
            node = queue.popleft()
            paths = paths_to_target[node]
            for next_node in reverse_nodes[node]:
                if next_node == start:
                    count += paths
                elif next_node in reachable_nodes:
                    next_paths_to_target.setdefault(next_node, 0)
                    next_paths_to_target[next_node] += paths
                    next_queue.append(next_node)
        queue = next_queue
        paths_to_target = next_paths_to_target
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
