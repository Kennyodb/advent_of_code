import re, sys, os, copy, itertools

TEST = False


def main():
    with open('test_input' if TEST else 'input', 'r') as f:
        input = f.readlines()
    print('input:')
    print(input)

    rules = []
    for i in range(len(input)):
        if len(input[i].split()) == 0:
            whiteline = i
            break
        split = input[i].strip().split("|")
        rules.append((int(split[0]), int(split[1])))

    rules.sort(key=first_element)
    print(rules)

    orders = []
    for i in range(whiteline + 1, len(input)):
        orders.append([])
        split = input[i].strip().split(",")
        for e in split:
            orders[-1].append(int(e))
    print(len(orders))
    print(orders)

    count = 0
    for list in orders:
        if correct_order(list, rules):
            count = count + middle(list)
    print(count)

    incorrectly_ordered = []
    for list in orders:
        if not correct_order(list, rules):
            incorrectly_ordered.append(list)

    count = 0
    for list in incorrectly_ordered:
        ordered = fix_order(list, rules)
        count = count + middle(ordered)
        if not correct_order(ordered, rules):
            print("AAAAAAAAAAAAAAAAAH")
        print(str(ordered) + " -> " + str(middle(ordered)))
    print(count)


def fix_order(list, rules):
    return insert([], list, rules)


def insert(list, to_insert, rules):
    if len(to_insert) == 0:
        return list

    to_insert = copy.deepcopy(to_insert)
    e = to_insert.pop()
    possibilities = get_valid_insertions(list, e, rules)
    for poss in possibilities:
        result = insert(poss, to_insert, rules)
        if result is not None:
            return result
    return None


def get_valid_insertions(list, e, rules):
    valid = []
    for i in range(len(list) + 1):
        option = copy.deepcopy(list)
        option.insert(i, e)
        if correct_order(option, rules):
            valid.append(option)
    return valid


def correct_order(list, rules):
    for rule in rules:
        if not is_applied(list, rule):
            return False
    return True


def is_applied(list, rule):
    return rule[0] not in list or rule[1] not in list \
        or list.index(rule[0]) < list.index(rule[1])


def middle(list):
    return list[int(len(list) / 2)]


def first_element(item):
    return item[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
