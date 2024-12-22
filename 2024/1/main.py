import re, sys, os, operator

TEST = False

def main():
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.readlines()
    print('input:')
    print(input)

    c0 = [int(e.strip().split("   ")[0]) for e in input]
    c1 = [int(e.strip().split("   ")[1]) for e in input]
    c0.sort()
    c1.sort()
    print(c0)
    print(c1)

    d = 0
    for i in range(len(c0)):
        d = d + abs(c0[i] - c1[i])

    print(d)

    #2
    sim = 0
    for i in range(len(c0)):
        sim = sim + (c0[i] * c1.count(c0[i]))
    print(sim)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
