import re, sys, os, copy, dataclasses, time, math


TEST = False
def main():
    start_time = time.perf_counter()
    with open('test_input' if TEST else 'input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    width = 101
    height = 103
    if TEST:
        width = 11
        height = 7

    robots = []
    for line in input:
        space = line.split(" ")
        pos = space[0].split(",")
        vel = space[1].split(",")
        posX = int(pos[0][2:])
        posY = int(pos[1])
        velX = int(vel[0][2:])
        velY = int(vel[1])
        robots.append([posX, posY, velX, velY])
    print(robots)

    steps = 10000
    for step in range(steps):
        do_step(robots, width, height)
        print(step)
        print_grid(robots, width, height)

    q0 = count_robots_between(robots, 0, 0, int(width / 2), int(height / 2))
    q1 = count_robots_between(robots, int(width / 2) + 1, 0, width, int(height / 2))
    q2 = count_robots_between(robots, int(width / 2) + 1, int(height / 2) + 1, width, height)
    q3 = count_robots_between(robots, 0, int(height / 2) + 1, int(width / 2), height)

    print(q0)
    print(q1)
    print(q2)
    print(q3)
    print(q0*q1*q2*q3)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def count_robots_between(robots, minX, minY, maxX, maxY):
    count = 0
    for robot in robots:
        if minX <= robot[0] < maxX and minY <= robot[1] < maxY:
            count += 1
    return count

def do_step(robots, width, height):
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % width
        robot[1] = (robot[1] + robot[3]) % height


def print_grid(robots, width, height):
    grid = [[' '] * width for i in range(height)]
    for robot in robots:
        grid[robot[1]][robot[0]] = '#'
    for line in grid:
        print(''.join(line))
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
