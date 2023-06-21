from collections import Counter
import time
import itertools

def swapPos(word, x, y):
    word = list(word)
    s_letter = word[x]
    word[x] = word[y]
    word[y] = s_letter
    return ''.join(word)

def swapLet(word, x, y):
    word = list(word)
    for i in range(len(word)):
        if word[i] == x:
            word[i] = y
        elif word[i] == y:
            word[i] = x
    return ''.join(word)

def rotateL(word, n):
    word = list(word)
    word = word[(n%len(word)):] + word[:(n%len(word))]
    return ''.join(word)

def rotateR(word, n):
    word = list(word)
    word = word[-(n%len(word)):] + word[:-(n%len(word))]
    return ''.join(word)

def rotateLetter(word, l):
    i = word.index(l)
    if i < 4:
        word = rotateR(word, i + 1)
    else:
        word = rotateR(word, i + 2)
    return word

def rotateLetter2(word, l):
    i = word.index(l)
    if i < 4:
        word = rotateL(word, i + 1)
    else:
        word = rotateL(word, i + 2)
    return word

def move(word, x, y):
    word = list(word)
    l = word[x]
    del word[x]
    word = word[:y] + [l] + word[y:]
    return ''.join(word)

def solve1():
    # botNum = 3
    # word = 'abcde'
    word = 'abcdefgh'
    allOrders = []

    with open("input", "r") as filestream:
        [allOrders.append(o[:-1]) for o in filestream]
        i = 0
        while i < len(allOrders):
            orders = allOrders[i].split()

            
            # print orders
            if orders[0] == 'swap' and orders[1] == 'position':
                word = swapPos(word, int(orders[2]), int(orders[5]))
            elif orders[0] == 'swap' and orders[1] == 'letter':
                word = swapLet(word, orders[2], orders[5])
            elif orders[0] == 'rotate' and orders[1] == 'left':
                word = rotateL(word, int(orders[2]))
            elif orders[0] == 'rotate' and orders[1] == 'right':
                word = rotateR(word, int(orders[2]))
            elif orders[0] == 'rotate' and orders[1] == 'based':
                word = rotateLetter(word, orders[6])
            elif orders[0] == 'reverse':
                word = word[:int(orders[2])] + word[int(orders[2]):int(orders[4]) + 1][::-1] + word[int(orders[4]) + 1:]
            elif orders[0] == 'move':
                word = move(word, int(orders[2]), int(orders[5]))
            # print word

            i += 1

    print word

def solve2():
    # botNum = 3
    # word = 'abcde'
    
    allOrders = []

    with open("input", "r") as filestream:
        [allOrders.append(o[:-1]) for o in filestream]
        
        res = ''
        word = 'abcdefgh'

        for word in itertools.product(word, repeat = 8):
            word = ''.join(word)
            if (len(set(word)) != len(word)):
                continue

            # print word
            res = word
            i = 0


            while i < len(allOrders):
                orders = allOrders[i].split()
                # print word
                
                # print orders
                if orders[0] == 'swap' and orders[1] == 'position':
                    word = swapPos(word, int(orders[2]), int(orders[5]))
                elif orders[0] == 'swap' and orders[1] == 'letter':
                    word = swapLet(word, orders[2], orders[5])
                elif orders[0] == 'rotate' and orders[1] == 'left':
                    word = rotateL(word, int(orders[2]))
                elif orders[0] == 'rotate' and orders[1] == 'right':
                    word = rotateR(word, int(orders[2]))
                elif orders[0] == 'rotate' and orders[1] == 'based':
                    word = rotateLetter(word, orders[6])
                elif orders[0] == 'reverse':
                    word = word[:int(orders[2])] + word[int(orders[2]):int(orders[4]) + 1][::-1] + word[int(orders[4]) + 1:]
                elif orders[0] == 'move':
                    word = move(word, int(orders[2]), int(orders[5]))
                # print word

                i += 1

            if word == 'fbgdceah':
                break

        print res

# solve1()
solve2()