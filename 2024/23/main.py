import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    connections = {}
    for line in input:
        computers = line.split("-")
        connections.setdefault(computers[0], set()).add(computers[1])
        connections.setdefault(computers[1], set()).add(computers[0])

    sets_by_size = [set()]
    sets_by_size[0].add(frozenset())
    current_size = 1
    while True:
        sets = set()
        for item in connections.items():
            c1 = item[0]
            c1_connections = item[1]
            for prev_set in sets_by_size[current_size - 1]:
                if all(c2 in c1_connections for c2 in prev_set):
                    new_set = set(prev_set)
                    new_set.add(c1)
                    sets.add(frozenset(new_set))
        if len(sets) == 0:
            break
        print(str(len(sets)) + " sets of size " + str(current_size))
        sets_by_size.append(sets)
        current_size += 1

    largest = list(list(sets_by_size[-1])[0])
    largest.sort()
    print(",".join(largest))

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
