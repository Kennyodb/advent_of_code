import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('test_input' if TEST else 'input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    complexities = 0
    for i in input:
        print(i)
        seq = solve_all(i)
        print("".join(seq))
        print(len(seq))
        complexities += (len(seq) * int(i[:-1]))
        print()

    print(complexities)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def solve_all(input):
    solutions = []
    prev_character = 'A'
    for character in input:
        r1_sequences = solve_numeric(character, prev_character)
        prev_character = character
        r2_sequences = []
        for i1 in r1_sequences:
            r2_sequences.extend(solve_directional(i1))
        r3_sequences = []
        for i2 in r2_sequences:
            r3_sequences.extend(solve_directional(i2))
        solutions.extend(min(r3_sequences, key=len))

    return solutions


def all_shortest(sequences):
    sequences.sort(key=len)
    min_len = len(sequences[0])
    for i in range(1, len(sequences)):
        if len(sequences[i]) > min_len:
            return sequences[:i]
    return sequences



def solve_numeric(input, start_button):
    return solve(input, {
        '7': (0, 0),
        '8': (1, 0),
        '9': (2, 0),
        '4': (0, 1),
        '5': (1, 1),
        '6': (2, 1),
        '1': (0, 2),
        '2': (1, 2),
        '3': (2, 2),
        '0': (1, 3),
        'A': (2, 3),
    }, (0, 3), start_button)


def solve_directional(input):
    return solve(input, {
        '^': (1, 0),
        'A': (2, 0),
        '<': (0, 1),
        'v': (1, 1),
        '>': (2, 1),
    }, (0, 0))


def solve(input, buttons, avoid, start_button='A'):
    sequences = [[]]
    current = buttons.get(start_button)
    for character in input:
        target = buttons.get(character)
        dx = target[0] - current[0]
        dy = target[1] - current[1]
        illegal = None
        if current[1] == avoid[1] and target[0] == avoid[0]:
            illegal = ['<'] * -dx
        elif current[0] == avoid[0] and target[1] == avoid[1]:
            if dy < 0:
                illegal = ['^'] * -dy
            else:
                illegal = ['v'] * dy
        new_sequences = []
        for move_seq in get_move_sequences(dx, dy):
            list(move_seq)
            if illegal is None or not starts_with(move_seq, illegal):
                for seq in sequences:
                    new_sequences.append(seq + list(move_seq) + ['A'])
        sequences = new_sequences
        current = target
    return sequences


def get_move_sequences(dx, dy):
    seq = []
    if dx > 0:
        seq.extend(['>'] * dx)
    elif dx < 0:
        seq.extend(['<'] * -dx)
    if dy < 0:
        seq.extend(['^'] * -dy)
    elif dy > 0:
        seq.extend(['v'] * dy)
    return [list(perm) for perm in set(itertools.permutations(seq))]


def starts_with(array, start):
    for i in range(len(start)):
        if array[i] != start[i]:
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
