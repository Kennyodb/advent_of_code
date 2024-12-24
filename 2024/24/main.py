import re, sys, os, copy, dataclasses, time, math, itertools


TEST = False
def main():
    start_time = time.perf_counter()
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.read().splitlines()
    print('input:')
    # print(input)

    whiteline = next(i for i, line in enumerate(input) if len(line) == 0)

    vals = {}
    for i in range(whiteline):
        line = input[i].split(": ")
        vals[line[0]] = line[1] == '1'

    gates = {}
    for i in range(whiteline + 1, len(input)):
        line = input[i].split(" ")
        gates[line[4]] = line[:3]

    # vals = evaluate(vals, gates)

    #niks foefelare
    swap = [
        ("qff", "qnw"), # z11 main xor <> first overflow of z12
        ("pbv", "z16"), # full z16 <> first overflow of z17
        ("z23", "qqp"), # full z23  <> full overflow of z24
        ("z36","fbq") # full z36 <> unused??
    ]

    for s in swap:
        temp = gates.get(s[0])
        gates[s[0]] = gates.get(s[1])
        gates[s[1]] = temp

    has_errors = False
    i = 0
    while True:
        bit_index = str(i).zfill(2)
        z = "z" + bit_index
        if z not in gates:
            break
        logical_string = to_string(z, gates)[1:-1]
        print(z + " = " + logical_string)

        x = "x" + bit_index
        y = "y" + bit_index
        if not in_string(x, y, "xor", logical_string) and bit_index != '45': #hardcoded ignore last bit
            has_errors = True
            print(z + " is wrong! Doesn't contain main addition xor.") # z11 z16 z45
        for i2 in range(i):
            bit_index2 = str(i2).zfill(2)
            if not in_string("x" + bit_index2, "y" + bit_index2, "and", logical_string):
                has_errors = True
                print(z + " is wrong! Doesn't contain full overflow stack. Missing index: " + bit_index2)
        i += 1

    print()
    if has_errors:
        print("Errors were found...")
    else:
        print("SUCCESS!")
    print()

    print("Took " + str(time.perf_counter() - start_time) + " seconds")


def in_string(x,  y, op,string):
    return (x + " " + op + " " + y) in string or (y + " " + op + " " + x) in string

def evaluate(initial_vals, gates):
    vals = copy.deepcopy(initial_vals)
    while len(gates) > 0:
        remaining_gates = {}
        for gate in gates.items():
            v1 = vals.get(gate[1][0])
            v2 = vals.get(gate[1][2])
            if v1 is None or v2 is None:
                remaining_gates[gate[0]] = gate[1]
                continue
            if gate[1][1] == "AND":
                vals[gate[0]] = v1 and v2
            elif gate[1][1] == "OR":
                vals[gate[0]] = v1 or v2
            else:
                vals[gate[0]] = v1 ^ v2
        if len(gates) == len(remaining_gates):
            print("infinite loop! Remaining wires: " + str(len(gates)))
            break
        gates = remaining_gates
    return vals


def to_string(wire, gates):
    if wire[0] == 'x' or wire[0] == 'y':
        return wire
    gate = gates.get(wire)
    v1 = to_string(gate[0], gates)
    v2 = to_string(gate[2], gates)
    return "(" + v1 + " " + gate[1].lower() + " " + v2 + ")"


def gather_inputs(wire, gates, inputs):
    if wire[0] == 'x' or wire[0] == 'y':
        inputs.add(wire)
    else:
        gate = gates.get(wire)
        gather_inputs(gate[0], gates, inputs)
        gather_inputs(gate[2], gates, inputs)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
