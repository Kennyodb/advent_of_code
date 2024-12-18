import re, sys, os, copy, dataclasses, fractions


TEST = False
def main():
    with open('test_input' if TEST else 'input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    height = len(input)
    width = len(input[0].strip())
    antennas = {}
    for i in range(height):
        line = input[i].strip()
        for j in range(width):
            key = line[j]
            if key != '.':
                if key not in antennas:
                    antennas[key] = [(j, i)]
                else:
                    antennas[key].append((j, i))

    print(antennas)

    antinodes = set()
    for key in antennas:
        ants = antennas.get(key)
        for i in range(len(ants)):
            for j in range(i + 1, len(ants)):
                dx = ants[j][0] - ants[i][0]
                dy = ants[j][1] - ants[i][1]
                left = (ants[i][0] - dx, ants[i][1] - dy)
                right = (ants[j][0] + dx, ants[j][1] + dy)
                if is_on_grid(width, height, left):
                    antinodes.add(left)
                if is_on_grid(width, height, right):
                    antinodes.add(right)

    print(antinodes)
    print(len(antinodes))

    #pt2
    antinodes = set()
    for key in antennas:
        ants = antennas.get(key)
        for i in range(len(ants)):
            for j in range(i + 1, len(ants)):
                dx = ants[j][0] - ants[i][0]
                dy = ants[j][1] - ants[i][1]
                fraction = fractions.Fraction(dx, dy)
                dx = fraction.numerator
                dy = fraction.denominator

                antinodes.add(ants[i])
                antinodes.add(ants[j])

                left = (ants[i][0] - dx, ants[i][1] - dy)
                while is_on_grid(width, height, left):
                    antinodes.add(left)
                    left = (left[0] - dx, left[1] - dy)

                right = (ants[i][0] + dx, ants[i][1] + dy)
                while is_on_grid(width, height, right):
                    antinodes.add(right)
                    right = (right[0] + dx, right[1] + dy)

    print(antinodes)
    print(len(antinodes))


def is_on_grid(width, height, coord):
    return 0 <= coord[0] < width and 0 <= coord[1] < height


    #TODO

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
