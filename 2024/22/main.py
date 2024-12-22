import re, sys, os, copy, dataclasses, time, math, itertools


TEST = True
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    print(input)

    initial_secrets = [int(s) for s in input]

    all_prices = []
    for secret in initial_secrets:
        prices = [secret % 10]
        for i in range(2000):
            secret = next_secret(secret)
            prices.append(secret % 10)
        all_prices.append(prices)

    prices_by_seq = []
    for p in all_prices:
        price_by_seq = {}
        for i in range(4, len(p)):
            seq = (p[i-3] - p[i-4], p[i-2] - p[i-3], p[i-1] - p[i-2], p[i] - p[i-1])
            if seq not in price_by_seq:
                price_by_seq[seq] = p[i]
        prices_by_seq.append(price_by_seq)

    unique_seqs = set()
    for entry in prices_by_seq:
        unique_seqs.update(entry.keys())
    print(str(len(unique_seqs)) + " unique sequences")

    most_bananas = 0
    for seq in unique_seqs:
        bananas = 0
        for entry in prices_by_seq:
            val = entry.get(seq)
            if val is not None:
                bananas += val
        most_bananas = max(most_bananas, bananas)

    print(most_bananas)

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def next_secret(n):
    prune = 16777216
    n = (n ^ (n * 64)) % prune
    n = (n ^ int(n / 32)) % prune
    n = (n ^ (n * 2048)) % prune
    return n


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
