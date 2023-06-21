import hashlib

def iterTree(depth, psw, loc):
    h = hashlib.md5(psw).hexdigest()
    # print psw[8:]
    # print h[:4]
    # print loc
    res = None
    if ord(h[0]) > ord('a') and depth > 0 and loc[0] > 0 and res == None:
        res = iterTree(depth - 1, psw + 'U', [loc[0] - 1, loc[1]])
    if ord(h[1]) > ord('a') and depth > 0 and loc[0] < 3 and res == None:
        res = iterTree(depth - 1, psw + 'D', [loc[0] + 1, loc[1]])
    if ord(h[2]) > ord('a') and depth > 0 and loc[1] > 0 and res == None:
        res = iterTree(depth - 1, psw + 'L', [loc[0], loc[1] - 1])
    if ord(h[3]) > ord('a') and depth > 0 and loc[1] < 3 and res == None:
        res = iterTree(depth - 1, psw + 'R', [loc[0], loc[1] + 1])

    # print res
    if loc[0] == 3 and loc[1] == 3:
        # print 'HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEE'
        return psw
    else:
        return res


def solve1():
    passcode = 'hhhxzeay'
    loc = [0,0]
    depth = 0

    i = 0
    res = None
    while (res == None):
        res = iterTree(i, passcode, loc)
        i += 1
        
    print res[len(passcode):]





def iterTree2(depth, psw, loc):
    h = hashlib.md5(psw).hexdigest()
    # print psw[8:]
    # print h[:4]
    # print loc
    res = None
    if ord(h[0]) > ord('a') and depth > 0 and loc[0] > 0:
        i = iterTree2(depth - 1, psw + 'U', [loc[0] - 1, loc[1]])
        if res == None or i != None and res > i:
            res = i
        # if psw[8:] == 'D':
        #     print res
    if ord(h[1]) > ord('a') and depth > 0 and loc[0] < 3:
        i = iterTree2(depth - 1, psw + 'D', [loc[0] + 1, loc[1]])
        if res == None or i != None and res > i:
            res = i
        # if psw[8:] == 'D':
        #     print 'AAAAAAAAAAAAA'
        #     print res
    if ord(h[2]) > ord('a') and depth > 0 and loc[1] > 0:
        i = iterTree2(depth - 1, psw + 'L', [loc[0], loc[1] - 1])
        if res == None or i != None and res > i:
            res = i
        # if psw[8:] == 'D':

        #     print res
    if ord(h[3]) > ord('a') and depth > 0 and loc[1] < 3:
        # if psw[8:] == 'D':
        #     print 'CMOOOON'
        #     print res
        i = iterTree2(depth - 1, psw + 'R', [loc[0], loc[1] + 1])
        if res == None or i != None and res > i:
            res = i
        # if psw[8:] == 'D':
        #     print 'CMOOOON'
        #     print res
    # print psw[8:]
    # print res
    if loc[0] == 3 and loc[1] == 3:
        # print 'HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEE'
        return depth
    else:
        return res


def solve2():
    passcode = 'hhhxzeay'
    loc = [0,0]
    depth = 0
    maxDepth = 505

    i = 0
    res = iterTree2(maxDepth, passcode, loc)
        
    print maxDepth - res

# solve1()
solve2()