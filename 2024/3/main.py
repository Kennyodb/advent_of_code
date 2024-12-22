import re

def main():
    with open('input', 'r') as f:
        s = f.read()
    print(s)

    muls = re.findall('mul\\(\\d+,\\d+\\)', s)
    print(len(muls))
    numbers = [e[4:-1] for e in muls]
    products = [int(e.split(',')[0]) * int(e.split(',')[1]) for e in numbers]
    print(products)
    print(sum(products))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
