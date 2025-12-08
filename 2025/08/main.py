import re, sys, os, copy, dataclasses, time, math, itertools
from sortedcontainers import SortedDict


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    all_nodes = []
    for line in input:
        split = line.split(",")
        all_nodes.append((int(split[0]), int(split[1]), int(split[2])))

    distances = dict() # squared
    for i in range(len(all_nodes)):
        for j in range(i+1, len(all_nodes)):
            d = pythagoras(all_nodes[i], all_nodes[j])
            if distances.get(d) is None:
                distances[d] = [(all_nodes[i], all_nodes[j])]
            else:
                distances.get(d).append((all_nodes[i], all_nodes[j]))

    sorted_distances = sorted(distances.keys())
    clusters = dict()
    clusters[1] = []
    for node in all_nodes:
        s = set()
        s.add(node)
        clusters[1].append(s)
    for d in sorted_distances:
        nodes = distances.get(d)[0]
        c1 = find_cluster(clusters, nodes[0])
        c2 = find_cluster(clusters, nodes[1])
        if c1 == c2:
            continue
        new_size = len(c1) + len(c2)
        new_set = set()
        new_set.update(c1)
        new_set.update(c2)
        if clusters.get(new_size) is None:
            clusters[new_size] = []
        clusters.get(new_size).append(new_set)
        clusters.get(len(c1)).remove(c1)
        clusters.get(len(c2)).remove(c2)
        if is_only_one_cluster(clusters):
            print(nodes)
            print(nodes[0][0] * nodes[1][0])
            break

    # non_empty_clusters = [size for size in clusters if len(clusters[size]) > 0]
    # sorted_clusters = sorted(non_empty_clusters, reverse=True)
    # print(sorted_clusters[0] * sorted_clusters[1] * sorted_clusters[2])

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def is_only_one_cluster(clusters):
    count = 0
    for level in clusters.items():
        if len(level[1]) > 1:
            return False
        elif len(level[1]) == 1:
            if count > 0:
                return False
            else:
                count = 1
    return count == 1

def find_cluster(clusters, node):
    for level in clusters.items():
        for cluster in level[1]:
            if node in cluster:
                return cluster
    raise Exception("No cluster found")


def pythagoras(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
