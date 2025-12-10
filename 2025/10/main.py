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
    for machine in range(len(expected_lights)):
        buttons = [(b,i) for b,i in enumerate(all_buttons[machine])]
        buttons = sorted(buttons, key=lambda b: len(b), reverse=True)
        target = tuple(joltage[machine])
        current = tuple([0 for _ in range(len(target))])
        min_presses = solve(current, 0, target, buttons)
        print(min_presses)
        result += min_presses



    # -- attempt 3
    applicable_buttons = []
    for i in range(len(target)):
        applicable_buttons.append([])
        for button in buttons:
            if i in button:
                applicable_buttons[-1].append(button)
    solution = [None for _ in range(len(target))]
    solve2(solution, target, applicable_buttons)

    print(result)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")



def solve2(presses, target, applicable_buttons):
    if not None in presses:
        return sum(presses)
    if len(buttons) == 0:
        return -1
    max_presses = get_max_presses(buttons[0], current_state, target)
    for presses in range(max_presses, -1, -1):
        next_state = press(current_state, buttons[0], presses)
        next_presses = current_presses + presses
        if next_state == target:
            return next_presses
        solve_rest = solve(next_state, next_presses, target, buttons[1:])
        if solve_rest >= 0:
            return solve_rest
    return -1


def solve(current_state, current_presses, target, buttons):
    if len(buttons) == 0:
        return -1
    max_presses = get_max_presses(buttons[0], current_state, target)
    for presses in range(max_presses, -1, -1):
        next_state = press(current_state, buttons[0], presses)
        next_presses = current_presses + presses
        if next_state == target:
            return next_presses
        solve_rest = solve(next_state, next_presses, target, buttons[1:])
        if solve_rest >= 0:
            return solve_rest
    return -1


def press(current, button, nb_presses):
    next_state = list(current)
    for i in button:
        next_state[i] += nb_presses
    return tuple(next_state)


def get_max_presses(button, current, target):
    presses = [target[i] - current[i] for i in button]
    return min(presses)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
