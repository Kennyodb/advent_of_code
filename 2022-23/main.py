import copy
import re, sys, os, dataclasses


TEST = False

@dataclasses.dataclass
class Elf:
    x: int
    y: int
    # order = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    # order = ['N', 'S', 'W', 'E']

def main():
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.readlines()
    print('input:')
    print(input)

    elves = []
    for j in range(len(input)):
        line = input[j]
        for i in range(len(line)):
            if line[i] == '#':
                elves.append(Elf(i, len(input)-j))
    print(elves)

    print_elves(elves)
    round_number = 0
    moved = True
    while moved:
        moved = False
        proposals = get_proposals(elves, get_proposal_order(round_number))
        proposal_counts = {}
        for proposal in proposals:
            count = proposal_counts.get(proposal)
            if count is None:
                proposal_counts[proposal] = 1
            else:
                proposal_counts[proposal] = count + 1

        for i in range(len(elves)):
            elf = elves[i]
            proposal = proposals[i]
            if proposal_counts.get(proposal) == 1:
                moved = True
                elf.x = proposal[0]
                elf.y = proposal[1]
        # print_elves(elves)
        round_number += 1
        print(round_number)

    print_elves(elves)

    bbox = get_bbox(elves)
    print(bbox)
    width = bbox[2] - bbox[0] + 1
    height = bbox[3] - bbox[1] + 1
    print(width * height - len(elves))


def print_elves(elves):
    bbox = get_bbox(elves)
    width = bbox[2] - bbox[0] + 1
    height = bbox[3] - bbox[1] + 1
    print()
    for j in range(height):
        line = ["."] * (width)
        for i in range(width):
            if is_occupied(bbox[0] + i, bbox[3] - j, elves):
                line[i] = '#'
        print("".join(line))
    print()


def get_bbox(elves):
    min_x = min([elf.x for elf in elves])
    max_x = max([elf.x for elf in elves])
    min_y = min([elf.y for elf in elves])
    max_y = max([elf.y for elf in elves])
    return [min_x, min_y, max_x, max_y]


def get_proposal_order(round_number):
    if round_number % 4 == 0:
        return ['N', 'S', 'W', 'E']
    elif round_number % 4 == 1:
        return ['S', 'W', 'E', 'N']
    elif round_number % 4 == 2:
        return ['W', 'E', 'N', 'S']
    else:
        return ['E', 'N', 'S', 'W']


def get_proposals(elves, order):
    proposals = []
    for elf in elves:
        proposals.append(get_proposal(elf, order, elves))
    return proposals


def get_proposal(elf, order, elves):
    if not has_elves_adjacent(elf, elves):
        return None
    for direction in order:
        if not has_elves_in_direction(elf, direction, elves):
            return get_square_in_direction(elf, direction)
    return None


def get_square_in_direction(elf, direction):
    if direction == 'N':
        return elf.x, elf.y + 1
    elif direction == 'S':
        return elf.x, elf.y - 1
    elif direction == 'W':
        return elf.x - 1, elf.y
    elif direction == 'E':
        return elf.x + 1, elf.y
    else:
        raise Exception(direction)


def has_elves_in_direction(elf, direction, elves):
    if direction == 'N':
        return is_occupied(elf.x-1, elf.y+1, elves) \
            or is_occupied(elf.x, elf.y+1, elves) \
            or is_occupied(elf.x+1, elf.y+1, elves)
    elif direction == 'S':
        return is_occupied(elf.x-1, elf.y-1, elves) \
            or is_occupied(elf.x, elf.y-1, elves) \
            or is_occupied(elf.x+1, elf.y-1, elves)
    elif direction == 'W':
        return is_occupied(elf.x-1, elf.y-1, elves) \
            or is_occupied(elf.x-1, elf.y, elves) \
            or is_occupied(elf.x-1, elf.y+1, elves)
    elif direction == 'E':
        return is_occupied(elf.x+1, elf.y-1, elves) \
            or is_occupied(elf.x+1, elf.y, elves) \
            or is_occupied(elf.x+1, elf.y+1, elves)
    else:
        raise Exception(direction)

def has_elves_adjacent(elf, elves):
    return is_occupied(elf.x-1, elf.y-1, elves) \
        or is_occupied(elf.x-1, elf.y, elves) \
        or is_occupied(elf.x-1, elf.y+1, elves) \
        or is_occupied(elf.x, elf.y-1, elves) \
        or is_occupied(elf.x, elf.y+1, elves) \
        or is_occupied(elf.x+1, elf.y-1, elves) \
        or is_occupied(elf.x+1, elf.y, elves) \
        or is_occupied(elf.x+1, elf.y+1, elves)

def is_occupied(x, y, elves):
    for elf in elves:
        if elf.x == x and elf.y == y:
            return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
