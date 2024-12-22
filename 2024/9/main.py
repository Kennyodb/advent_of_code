import re, sys, os, copy, dataclasses


TEST = False

def main():
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    blocks = []
    for i in range(len(input[0])):
        b = i / 2 if i % 2 == 0 else -1
        for i in range(int(input[0][i])):
            blocks.append(b)
    print(blocks)

    leftmost_free = find_leftmost_free_block_id(blocks, 0)
    i = len(blocks) - 1
    while i >= leftmost_free:
        if blocks[i] >= 0:
            size = get_size_reverse(blocks, i)
            start_of_file = i - size + 1
            dest = find_leftmost_free_of_size(blocks, leftmost_free, size)
            if dest < start_of_file:
                swap_multiple(blocks, dest, start_of_file, size)
                leftmost_free = find_leftmost_free_block_id(blocks, leftmost_free)
            i -= size
        else:
            i -= 1

    print(blocks)
    print(checksum(blocks))


def get_size(blocks, i):
    id = blocks[i]
    size = 0
    while i < len(blocks) and blocks[i] == id:
        size += 1
        i += 1
    return size

def get_size_reverse(blocks, i):
    id = blocks[i]
    size = 0
    while i >= 0 and blocks[i] == id:
        size += 1
        i -= 1
    return size

def find_leftmost_free_block_id(blocks, start):
    i = start
    while i < len(blocks) and blocks[i] >= 0:
        i += 1
    return i


def find_leftmost_free_of_size(blocks, start, size):
    i = find_leftmost_free_block_id(blocks, start)
    while i < len(blocks):
        free_size = get_size(blocks, i)
        if free_size >= size:
            break
        i = find_leftmost_free_block_id(blocks, i + free_size)
    return i


def swap(blocks, i0, i1):
    temp = blocks[i0]
    blocks[i0] = blocks[i1]
    blocks[i1] = temp


def swap_multiple(blocks, i0, i1, size):
    for i in range(size):
        swap(blocks, i0 + i, i1 + i)


def checksum(blocks):
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] >= 0:
            checksum += i * blocks[i]
    return checksum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
