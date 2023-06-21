import hashlib

def solve1():
    door = 'ugkcyxxp'
    i = 0
    res = ''
    while (len(res) < 8):
        h = hashlib.md5(door + str(i)).hexdigest()
        if (h[:5] == '00000'):
            res += h[5]
        i += 1;
        
    print res

def solve2():
    door = 'ugkcyxxp'
    i = 0
    amount = 0
    res = [None] * 8
    while (amount < 8):
        h = hashlib.md5(door + str(i)).hexdigest()
        if (h[:5] == '00000'):
            if (h[5].isdigit() and int(h[5]) < 8 and res[int(h[5])] == None):
                res[int(h[5])] = h[6]
                amount += 1
                print res[int(h[5])]
        i += 1;
        
    print ''.join(res)

# solve1()
solve2()
# print 'a'.isdigit()