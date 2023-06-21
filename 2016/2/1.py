def solve():
    x = 0
    y = 0
    d = 0
    xfin = -1
    yfin = -1
    result = []
    with open("input", "r") as filestream:
        for line in filestream:
            for order in line:
                x, y = calculate2(order, x, y)
            print x, y
            #result.append(5 + x + (-3*y))
            r = 5 + x + (-4*y)
            if (r == 10):
                r = 'A'
            elif (r == 11):
                r = 'B'
            elif (r == 12):
                r = 'C'
            elif (r == 15):
                r = 'D'

            result.append(r)



        print result


def calculate2(orde, x, y):
    if (orde == 'U' and abs(x - 2) + abs(y + 1) != 3):
        y += 1
    elif (orde == 'R' and abs(x - 1) + abs(y) != 3):
        x += 1
    elif (orde == 'D' and abs(x - 2) + abs(y - 1) != 3):
        y -= 1
    elif (orde == 'L' and abs(x - 3) + abs(y) != 3):
        x -= 1
    return x, y

def calculate(orde, x, y):
    if (orde == 'U' and y != 1):
        y += 1
    elif (orde == 'R' and x != 1):
        x += 1
    elif (orde == 'D' and y != -1):
        y -= 1
    elif (orde == 'L' and x != -1):
        x -= 1
    return x, y

    #print y, x
solve()