import re, sys, os


TEST = False
def main():
    with open('../test_input' if TEST else '../input', 'r') as f:
        input = f.readlines()
    print('input:')
    print(input)

    width = len(input[0].strip())
    height = len(input)
    print(width)
    print(height)

    count = 0
    #right
    for j in range(height):
        for i in range(width-3):
            if input[j][i] == 'X' and input[j][i+1] == 'M' and input[j][i+2] == 'A' and input[j][i+3] == 'S':
                count = count + 1
    #down-right
    for j in range(height-3):
        for i in range(width-3):
            if input[j][i] == 'X' and input[j+1][i+1] == 'M' and input[j+2][i+2] == 'A' and input[j+3][i+3] == 'S':
                count = count + 1
    #down
    for j in range(height-3):
        for i in range(width):
            if input[j][i] == 'X' and input[j+1][i] == 'M' and input[j+2][i] == 'A' and input[j+3][i] == 'S':
                count = count + 1
    #down-left
    for j in range(height-3):
        for i in range(3, width):
            if input[j][i] == 'X' and input[j+1][i-1] == 'M' and input[j+2][i-2] == 'A' and input[j+3][i-3] == 'S':
                count = count + 1
    #left
    for j in range(height):
        for i in range(3, width):
            if input[j][i] == 'X' and input[j][i-1] == 'M' and input[j][i-2] == 'A' and input[j][i-3] == 'S':
                count = count + 1
    #up-left
    for j in range(3, height):
        for i in range(3, width):
            if input[j][i] == 'X' and input[j-1][i-1] == 'M' and input[j-2][i-2] == 'A' and input[j-3][i-3] == 'S':
                count = count + 1
    #up
    for j in range(3, height):
        for i in range(width):
            if input[j][i] == 'X' and input[j-1][i] == 'M' and input[j-2][i] == 'A' and input[j-3][i] == 'S':
                count = count + 1
    #up-right
    for j in range(3, height):
        for i in range(width-3):
            if input[j][i] == 'X' and input[j-1][i+1] == 'M' and input[j-2][i+2] == 'A' and input[j-3][i+3] == 'S':
                count = count + 1

    print(count)


    ### 2 ###

    count = 0
    #down-right
    for j in range(height-2):
        for i in range(width-2):
            if input[j+1][i+1] == 'A' and \
                    (input[j][i] == 'M' and input[j+2][i+2] == 'S' or input[j][i] == 'S' and input[j+2][i+2] == 'M') and \
                    (input[j][i+2] == 'M' and input[j+2][i] == 'S' or input[j][i+2] == 'S' and input[j+2][i] == 'M'):
                print(str(j) + ', ' + str(i))
                count = count + 1

    print(count)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
