from collections import Counter

def solve1():
    result = 0
    with open("input", "r") as filestream:
        for line in filestream:
            result = decompress (line)
            result2 = decompress2 (line)
    print result
    print result2

def decompress(line):
    result = 0
    ix = False
    iy = False
    x = ''
    y = ''
    skip = 0
    for c in line:
        if skip != 0:
            skip -= 1
            continue
        if c == '(':
            ix = True
        elif c == 'x':
            ix = False
            iy = True
        elif c == ')':
            result -= 1
            skip = int(x[1:])
            result += int(x[1:]) * int(y[1:])
            iy = False
            x = ''
            y = ''
        if ix:
            result -= 1
            x += c
        elif iy:
            result -= 1
            y += c
        result += 1
    return result

def decompress2(line):
    result = 0
    ix = False
    iy = False
    x = ''
    y = ''
    skip = 0
    inner = ''
    multi = 0
    for c in line:
        if skip != 0:
            inner += c
            skip -= 1
            if skip == 0:
                result += multi * decompress2(inner)
                multi = 0
                inner = ''
            continue
        if c == '(':
            ix = True
        elif c == 'x':
            ix = False
            iy = True
        elif c == ')':
            result -= 1
            skip = int(x[1:])
            multi = int(y[1:])
            iy = False
            x = ''
            y = ''
        if ix:
            result -= 1
            x += c
        elif iy:
            result -= 1
            y += c
        result += 1
    return result


solve1()