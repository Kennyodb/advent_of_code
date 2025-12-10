import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    expected_lights = []
    all_buttons = []
    joltage = []
    for line in input:
        split = line.split(' ')
        expected_lights.append(tuple([c == '#' for c in split[0][1:-1]]))
        joltage.append([int(l) for l in split[-1][1:-1].split(',')])
        buttons = []
        for i in range(1, len(split)-1):
            buttons.append([int(l) for l in split[i][1:-1].split(',')])
        all_buttons.append(buttons)

    # --- solution 1
    # result = 0
    # for machine in range(len(expected_lights)):
    #     expected = expected_lights[machine]
    #     buttons = all_buttons[machine]
    #     visited = [set()]
    #     visited[0].add(tuple([False for _ in range(len(expected))]))
    #     iteration = 0
    #     while not expected in visited[-1]:
    #         iteration += 1
    #         visited.append(set())
    #         for button in buttons:
    #             for start_lights in visited[-2]:
    #                 next_lights = list(start_lights)
    #                 for i in button:
    #                     next_lights[i] = not next_lights[i]
    #                 visited[-1].add(tuple(next_lights))
    #     result += iteration


    # --- solution 2

    result = 0
    starting_from = 53
    total = 1
    print('starting from: ', starting_from)
    for machine in range(starting_from, starting_from + total + 1):
        # print(machine)
        # if machine == 53 or machine == 90 or machine == 76:
        #     continue
        buttons = sorted(all_buttons[machine], key=lambda b: len(b), reverse=True)
        target = tuple(joltage[machine])
        state = tuple([0 for _ in range(len(target))])
        presses = [-1 for _ in range(len(buttons))]
        solutions = []
        min_presses = solve(state, presses, target, buttons, solutions, outer=True)
        minsol = min(solutions)
        if minsol != solutions[0]:
            print('!!! ---- ', minsol)
        else:
            print(minsol)
        result += min_presses

    print(result)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def solve(state, button_presses, target, buttons, solutions, outer=False):
    if min(button_presses) >= 0:
        if state == target:
            solutions.append(sum(button_presses))
            print('solution: ', sum(button_presses))
        return -1

    # early-out, or find target digit with a single applicable button
    for i in range(len(target)):
        diff = target[i] - state[i]
        applicable_buttons = []
        for button_i in range(len(buttons)):
            if button_presses[button_i] < 0 and i in buttons[button_i]:
                applicable_buttons.append(button_i)
        if len(applicable_buttons) == 0 and diff > 0:
            return -1
        if len(applicable_buttons) == 1:
            button_i = applicable_buttons[0]
            next_state = press(state, buttons[button_i], diff)
            if is_too_far(next_state, target):
                return -1
            next_presses = copy.deepcopy(button_presses)
            next_presses[button_i] = diff
            return solve(next_state, next_presses, target, buttons, solutions)

    button_i = find_first(-1, button_presses)
    max_presses = get_max_presses(buttons[button_i], state, target)
    next_presses = copy.deepcopy(button_presses)
    if outer:
        for presses in range(22, max_presses):
            print(presses)
            next_state = press(state, buttons[button_i], presses)
            next_presses[button_i] = presses
            solve_rest = solve(next_state, next_presses, target, buttons, solutions)
            if solve_rest >= 0:
                return solve_rest
    else:
        for presses in range(max_presses, -1, -1):
            next_state = press(state, buttons[button_i], presses)
            next_presses[button_i] = presses
            solve_rest = solve(next_state, next_presses, target, buttons, solutions)
            if solve_rest >= 0:
                return solve_rest

    return -1


def press(current, button, nb_presses):
    next_state = list(current)
    for i in button:
        next_state[i] += nb_presses
    return tuple(next_state)


def is_too_far(state, target):
    return any([state[i] > target[i] for i in range(len(state))])


def get_max_presses(button, current, target):
    presses = [target[i] - current[i] for i in button]
    return min(presses)


def find_first(element, list):
    for i, e in enumerate(list):
        if element == e:
            return i
    return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
