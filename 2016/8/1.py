from collections import Counter

def rect(box, size):
    for i in range(int(size[1])):
        for j in range(int(size[0])):
            # printBox(box)
            box[i][j] = '#'
    return box

def rotate(box, direction, index, rotateNum):
    if direction == 'x':
        # rotateLine = box[index][:]
        rotateLine = [row[index] for row in box]
        # print rotateLine
        fp = rotateLine[:-rotateNum]
        sp = rotateLine[-rotateNum:]
        # print fp
        # print sp
        newRotateLine = sp + fp
        for row in range(len(box)):
            box[row][index] = newRotateLine[row]
        # printBox(box)
    elif direction == 'y':
        rotateLine = box[:][index]
        # print rotateLine
        fp = rotateLine[:-rotateNum]
        sp = rotateLine[-rotateNum:]
        # print fp
        # print sp
        box[index] = sp + fp
        # for row in range(len(box)):
            # box[row][index] = newRotateLine[row]
        # printBox(box)
    return box



def printBox(box):
    for el in box:
        print ''.join(el)

def solve1():
    x = 50
    y = 6
    box = [['.']*x for _ in range(y)]
    # box = [['.'] * x] * y
    # printBox(box)
    result = 0
    with open("input", "r") as filestream:
        for line in filestream:
            orders = line.split()
            if orders[0] == 'rect':
                box = rect(box, orders[1].split('x'))
            elif orders[0] == 'rotate':
                box = rotate(box, orders[2][0],int(orders[2][2:]), int(orders[4]))

    printBox(box)
    for row in box:
        for el in row:
            if el == '#':
                result += 1
    print result

solve1()
# solve2()