from collections import Counter
import time

def cpy(registers, to, reg):
    if to.isdigit() or to.lstrip('-').isdigit():
        registers[reg] = int(to)
    else:
        registers[reg] = registers[ord(to) - ord('a')]
    return registers

def inc(registers, reg):
    registers[reg] += 1
    return registers

def dec(registers, reg):
    registers[reg] -= 1
    return registers

def jnz(i, registers, reg, jfor, listAllOrders):
    # if listAllOrders:
    # print jfor == -2
    # print listAllOrders[i-1]
    if jfor == -2 and i == 7 and listAllOrders[i-1][0] == 'dec' and listAllOrders[i-2][0] == 'inc':
        registers[0] += registers[2]
        registers[2] = 0
        return i, registers 
        # print 'AAAAAAAAAAAAA'

    if jfor == -2 and i == 15 and listAllOrders[i-1][0] == 'inc' and listAllOrders[i-2][0] == 'dec':
        registers[2] += registers[3]
        registers[3] = 0
        return i, registers 

    if jfor == -2 and i == 9:
        registers[0] += registers[1] * registers[3]
        registers[3] = 0
        return i, registers 


        # print 'AAAAAAAAAAAAA'


    if reg.isdigit() or reg.lstrip('-').isdigit():
        num = int(reg)
        if int(reg) > 0:
            i += jfor - 1
    else:
        num = ord(reg) - ord('a')
        # print num
        if registers[num] != 0:
            # print 'aAaAaAa'
            i += jfor - 1
    return i, registers

def tgl(listAllOrders, loc, dif):
    changeIndex = loc + dif
    # print changeIndex
    if changeIndex < 0 or changeIndex > len(listAllOrders)-1:
        return listAllOrders

    if listAllOrders[changeIndex][0] == 'inc':
        listAllOrders[changeIndex][0] = 'dec'
    elif listAllOrders[changeIndex][0] == 'dec' or listAllOrders[changeIndex][0] == 'tgl':
        listAllOrders[changeIndex][0] = 'inc'
    elif listAllOrders[changeIndex][0] == 'jnz':
        listAllOrders[changeIndex][0] = 'cpy'
    else:
        listAllOrders[changeIndex][0] = 'jnz'
    return listAllOrders


def solve1():
    registers = [0] * 4
    allOrders = []
    # P1
    registers[0] = 12
    # P2
    # registers[0] = 12

    with open("input2", "r") as filestream:
        [allOrders.append(o[:-1]) for o in filestream]
        i = 0
        listAllOrders = []

        


        for order in allOrders:
            listAllOrders.append(order.split())

        # P2
        i = 17
        registers[0] = 479001600
        registers[1] = 1
        registers[2] = 2
        registers[3] = 0
        listAllOrders[18][0] = 'cpy'
        listAllOrders[20][0] = 'cpy'
        listAllOrders[22][0] = 'dec'
        listAllOrders[24][0] = 'dec'


        #####################################

        while i < len(allOrders):
            orders = listAllOrders[i]

            # print orders
            # print i
            # print orders
            if orders[0] == 'cpy':
                if (not orders[2].isdigit()) and (not orders[2].lstrip('-').isdigit()):
                    registers = cpy(registers, orders[1], ord(orders[2]) - ord('a'))
            elif orders[0] == 'inc':
                registers = inc(registers, ord(orders[1]) - ord('a'))
            elif orders[0] == 'dec':
                registers = dec(registers, ord(orders[1]) - ord('a'))
            elif orders[0] == 'jnz':
                if orders[2].isdigit() or orders[2].lstrip('-').isdigit():
                    # print 'HEREEE', i
                    i, registers = jnz(i, registers, orders[1], int(orders[2]), listAllOrders)
                    # print 'AFTERR', i
                else:
                    i, registers = jnz(i, registers, orders[1], registers[ord(orders[2]) - ord('a')], listAllOrders)
            elif orders[0] == 'tgl':
                print orders
                print registers
                listAllOrders = tgl(listAllOrders, i, registers[ord(orders[1]) - ord('a')])

            
            # print orders
            # print ord(orders[1])
            # print ord('a')
            # print ord(orders[1]) - ord('a')
            # print registers
            # time.sleep(0.025)
            i += 1

            # if i == 8:
            #     break

    print registers[0]

solve1()
# solve2()