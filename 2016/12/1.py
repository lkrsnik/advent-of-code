from collections import Counter
import time

def cpy(registers, to, reg):
    if to.isdigit():
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

def jnz(i, registers, reg, jfor):
    if reg.isdigit():
        num = int(reg)
        if int(reg) > 0:
            i += jfor - 1
    else:
        num = ord(reg) - ord('a')
        if registers[num] > 0:
            i += jfor - 1
    return i


def solve1():
    # botNum = 3
    registers = [0] * 4
    allOrders = []
    registers[2] = 1
    # factory[0].append(3)
    # del factory[0][1]
    # print factory
    result = 1
    with open("input2", "r") as filestream:
        [allOrders.append(o[:-1]) for o in filestream]
        i = 0
        while i < len(allOrders):
            orders = allOrders[i].split()

            
            # print orders
            if orders[0] == 'cpy':
                registers = cpy(registers, orders[1], ord(orders[2]) - ord('a'))
            elif orders[0] == 'inc':
                registers = inc(registers, ord(orders[1]) - ord('a'))
            elif orders[0] == 'dec':
                registers = dec(registers, ord(orders[1]) - ord('a'))
            elif orders[0] == 'jnz':
                i = jnz(i, registers, orders[1], int(orders[2]))

            # print orders
            # print registers
            i += 1

    print(registers[0])

solve1()
# solve2()