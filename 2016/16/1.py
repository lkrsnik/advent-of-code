import hashlib, copy
def extend(a):
    res = copy.copy(a)
    b = ''
    for el in a:
        if el == '0':
            b += '1'
        else:
            b += '0'
    res = a + '0' + b[::-1]
    return res

def checksum(n):
    cs = ''
    for i in range(len(n)/2):
        if n[i*2] == n[(i*2)+1]:
            cs += '1'
        else:
            cs += '0'
    return cs

def solve1():
    n = '10010000000110000'
    l = 35651584
    while len(n) < l:
        n = extend(n)

    cs = checksum(n[:l])
    while len(cs) % 2 == 0:
        cs = checksum(cs)

    print cs
solve1()
# print 'a'.isdigit()

00111001111111101

