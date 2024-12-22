import re, sys, os, copy, dataclasses, time, math

TEST = False


def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    machines = []
    i = 0
    while i < len(input):
        ba = input[i].split(" ")
        bb = input[i + 1].split(" ")
        p = input[i + 2].split(" ")
        baX = int(ba[2][2:-1])
        baY = int(ba[3][2:])
        bbX = int(bb[2][2:-1])
        bbY = int(bb[3][2:])
        pX = int(p[1][2:-1]) + 10000000000000
        pY = int(p[2][2:]) + 10000000000000
        machines.append([baX, baY, bbX, bbY, pX, pY])
        i += 4
    print(machines)

    total = 0
    for machine in machines:
        solutions = get_solutions_but_without_all_the_dumb_stuff(machine)
        # real_solutions = get_solutions(machine)
        # if real_solutions != solutions:
        #     print("oh no!")
        #     get_solutions_but_without_all_the_dumb_stuff(machine)
        print(solutions)
        if len(solutions) > 0:
            total += min(solutions)
    print(total)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def get_solutions(machine):
    solutions = []
    for a in range(101):
        if (machine[4] - (a * machine[0])) % machine[2] == 0:
            b = int((machine[4] - (a * machine[0])) / machine[2])
            if a * machine[1] + b * machine[3] == machine[5]:
                print("solution: " + str(a) + "," + str(b) + " -> " + str(a * 3 + b))
                solutions.append(a * 3 + b)
    return solutions


def get_solutions_smarter(machine):
    solutions = []
    gcd_x = math.gcd(machine[0], machine[2])
    gcd_y = math.gcd(machine[1], machine[3])
    if machine[4] % gcd_x != 0 or machine[5] % gcd_y != 0:
        return []

    (a0, b0) = diop(machine[0], machine[2], machine[4])
    a0 = int(a0)
    b0 = int(b0)
    p = machine[0] // gcd_x
    q = machine[2] // gcd_x

    i = -int(a0 / q) - 1
    while True:
        a = a0 + i * q
        if a * machine[0] > machine[4]:
            break
        b = b0 - i * p
        if a >= 0 and b >= 0 and a * machine[1] + b * machine[3] == machine[5]:
            solutions.append(a * 3 + b)
        i += 1

    return solutions

def get_solutions_but_without_all_the_dumb_stuff(machine):
    # if (machine[1] * machine[4]) % machine[0] != 0 or:
    #     return []

    b = (machine[5] - (machine[1] * machine[4] / machine[0])) \
        / (machine[3] - (machine[1] * machine[2] / machine[0]))

    b_rounded = round(b)
    if b_rounded < 0 or abs(b - b_rounded) > 1e-4:
        return []

    a = machine[4] / machine[0] - machine[2] * b_rounded / machine[0]
    a_rounded = round(a)
    if a_rounded < 0 or abs(a - a_rounded) > 1e-4:
        return []

    return [a_rounded * 3 + b_rounded]

def diop(a, b, c):
    (d, x, y) = extended_gcd(a, b)
    r = int(c / d)
    return r * x, r * y


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)
    return d, x, y


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
