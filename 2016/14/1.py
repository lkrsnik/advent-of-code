import hashlib, copy

def solve1():
    repetedchars = []
    repetitions = 0
    salt = 'jlmsuwbz'
    keys = []
    i = 0
    while (len(keys) < 64):
        # h = hashlib.md5(salt + '22728').hexdigest()
        # print h
        h = hashlib.md5(salt + str(i)).hexdigest()
        pc = ''
        cr = 0
        nc = ''
        for c in h:
            if c == pc:
                cr += 1
            else:
                pc = c
                cr = 1
            if cr == 3 and nc == '':
                nc = c
            if cr == 5:
                # print i
                for rc in repetedchars:
                    
                    if(c == rc[0] and i-rc[1] < 1000):
                        repeted = False
                        for el in keys:
                            if el[1] == rc[1] and rc[0] == el[0]:
                                repeted = True
                        # print rc

                        if repeted:
                            continue
                        repetitions += 1
                        keys.append(rc)


        if nc != '':
            repetedchars.append([nc, i])
        i += 1

    keys.sort(key=lambda x: x[1])
    print keys[63]

def solve2():
    repetedchars = []
    repetitions = 0
    salt = 'jlmsuwbz'
    keys = []
    i = 0
    while (len(keys) < 64):
        # h = hashlib.md5(salt + '22728').hexdigest()
        # print h
        h = hashlib.md5(salt + str(i)).hexdigest()
        for j in range(2016):
            h = hashlib.md5(h).hexdigest()
        pc = ''
        cr = 0
        nc = ''
        for c in h:
            if c == pc:
                cr += 1
            else:
                pc = c
                cr = 1
            if cr == 3 and nc == '':
                nc = c
            if cr == 5:
                # print i
                for rc in repetedchars:
                    
                    if(c == rc[0] and i-rc[1] < 1000):
                        repeted = False
                        for el in keys:
                            if el[1] == rc[1] and rc[0] == el[0]:
                                repeted = True
                        # print rc

                        if repeted:
                            continue
                        repetitions += 1
                        keys.append(rc)


        if nc != '':
            repetedchars.append([nc, i])
        i += 1

    keys.sort(key=lambda x: x[1])
    print keys[63]

# solve1()

# 22551
solve2()
# print 'a'.isdigit()


