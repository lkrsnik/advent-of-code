

def solve1():
    with open("input3", "r") as filestream:
        orders = []
        for line in filestream:
            ws = line.split()
            orders.append([int(ws[3]), int(ws[-1][:-1])])

        i = 0
        res = -1
        while res != 0:
            res = 0
            ic = 0
            for j in range(len(orders)):
                ic += 1
                res += (ic + orders[j][1] + i) % orders[j][0]
            i += 1



    print i - 1


solve1()
