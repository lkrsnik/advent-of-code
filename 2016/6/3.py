from collections import Counter

def solve1():
    result = 0
    res = ''
    for el in list(zip(*[line.rstrip('\n') for line in open('input')])):
        res += list(Counter(''.join(el)).most_common())[0][0]
    print res
    

def solve2():
    result = 0
    res = ''
    for el in list(zip(*[line.rstrip('\n') for line in open('input')])):
        res += list(Counter(''.join(el)).most_common())[-1][0]
    print res

solve1()
solve2()