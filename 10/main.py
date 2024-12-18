import re, sys, os, copy, dataclasses, time


TEST = False
def main():
    start_time = time.perf_counter()
    with open('test_input' if TEST else 'input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    grid = [[int(e) for e in line] for line in input]
    print(grid)

    score = 0
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if row[j] == 0:
                tails = []
                get_trail_tails(grid, j, i, tails)
                score += len(tails)
    print(score)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def get_trail_tails(grid, x, y, results):
    val = grid[y][x]
    if val == 9:
        results.append((x, y))
        return
    if is_on_grid(grid, x-1, y) and grid[y][x-1] == val + 1:
        get_trail_tails(grid, x - 1, y, results)
    if is_on_grid(grid, x+1, y) and grid[y][x+1] == val + 1:
        get_trail_tails(grid, x + 1, y, results)
    if is_on_grid(grid, x, y-1) and grid[y-1][x] == val + 1:
        get_trail_tails(grid, x, y - 1, results)
    if is_on_grid(grid, x, y+1) and grid[y+1][x] == val + 1:
        get_trail_tails(grid, x, y + 1, results)



def is_on_grid(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
