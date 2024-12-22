import re, sys, os, copy, dataclasses, time, math

TEST = False


def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    stones = [int(e) for e in input[0].split(" ")]
    print(stones)


    stones_dict = {}
    for stone in stones:
        stones_dict[stone] = 1
    do_blinks_but_smarter(stones_dict, 75)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def do_step(stones, cache, step, reports, update_cache):
    report_step = int(len(stones) / reports)
    next_stones = []
    for i in range(len(stones)):
        stone = stones[i]
        if i % report_step == 0:
            print(str(round(100 * i / len(stones))) + "%")
        cached = cache.get(stone)
        if cached is not None:
            next_stones.extend(cached)
        else:
            value = do_blinks([stone], step)
            next_stones.extend(value)
            if update_cache:
                cache[stone] = value
    return next_stones


def do_blinks_but_smarter(stones, blinks):
    for i in range(blinks):
        stones = blink(stones)
        print(str(i+1) + ": " + str(sum(stones.values())))

def blink(stones):
    next_stones = {}
    for stone_entry in stones.items():
        stone = stone_entry[0]
        count = stone_entry[1]
        if stone == 0:
            increment(next_stones, 1, count)
        else:
            nb_digits = int(math.log10(stone)) + 1
            if nb_digits % 2 == 0:
                mid = int(nb_digits / 2)
                increment(next_stones,  int(stone / (10 ** mid)), count)
                increment(next_stones, stone % (10 ** mid), count)
            else:
                increment(next_stones, stone * 2024, count)
    return next_stones


def increment(dict, key, count):
    val = dict.get(key)
    if val is None:
        val = 0
    dict[key] = val + count


def do_blinks(stones, blinks):
    for blink in range(blinks):
        next_stones = []
        for stone in stones:
            if stone == 0:
                next_stones.append(1)
            else:
                nb_digits = int(math.log10(stone)) + 1
                if nb_digits % 2 == 0:
                    mid = int(nb_digits / 2)
                    next_stones.append(int(stone / (10 ** mid)))
                    next_stones.append(stone % (10 ** mid))
                else:
                    next_stones.append(stone * 2024)
        stones = next_stones
    return stones


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
