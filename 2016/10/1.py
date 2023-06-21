from collections import Counter

def goes(factory, val, bot):
    factory[bot].append(val)
    return factory

def gives(factory, bot, lv, hv, lvo, hvo):
    if lvo:
        lv = lv * (-1) - 1
    if hvo:
        hv = hv * (-1) - 1
    factory[bot].extend([lv, hv])
    return factory



def printBox(box):
    for el in box:
        print ''.join(el)

def solve1():
    # botNum = 3
    botNum = 210
    factory = [[a] for a in range(botNum)]
    # factory[0].append(3)
    # del factory[0][1]
    # print factory
    result = 1
    with open("input", "r") as filestream:
        for line in filestream:
            orders = line.split()

            if orders[2] == 'gives':
                factory = gives(factory, int(int(orders[1])),int(orders[6]), int(orders[11]),orders[5] == 'output', orders[10] == 'output')

    with open("input", "r") as filestream:
        for line in filestream:
            orders = line.split()
            if orders[2] == 'goes':
                factory = goes(factory, int(orders[1]), int(orders[5]))

    change = True
    # print factory
    while (change):
        change = False
        for bot in factory:
            if (len(bot) == 5):
                change = True
                if ((bot[4] == 17 and bot[3] == 61) or (bot[3] == 17 and bot[4] == 61)):
                    print bot
                if (bot[1] >= 0):
                    factory[bot[1]].append(min(bot[3], bot[4]))
                elif (bot[1] >= -3):
                    result *= min(bot[3], bot[4])
                if (bot[2] >= 0):
                    factory[bot[2]].append(max(bot[3], bot[4]))
                elif (bot[2] >= -3):
                    result *= max(bot[3], bot[4])
                del bot[4]
                del bot[3]

    
    # printBox(box)
    # for row in box:
    #     for el in row:
    #         if el == '#':
    #             result += 1
    print result

solve1()
# solve2()