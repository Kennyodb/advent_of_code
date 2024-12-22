import re, sys, os


TEST = False
def main():
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.readlines()
    print('input:')
    print(input)

    safecount = 0
    for line in input:
        if(safe(line.strip().split(" "))):
            safecount += 1
    print(safecount)

    supersafecount = 0
    for line in input:
        if(supersafe(line.strip().split(" "))):
            supersafecount += 1
    print(supersafecount)


def supersafe(list):
    for i in range(len(list)):
        subl = list[:i] + list[i+1:]
        if safe(subl):
            return True
    return False

def safe(list):
    increasing = int(list[1]) > int(list[0])
    for i in range(len(list) - 1):
        e0 = int(list[i])
        e1 = int(list[i+1])
        if increasing and e1 <= e0:
            return False
        if (not increasing) and e1 >= e0:
            return False
        if abs(e1 - e0) > 3:
            return False

    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
