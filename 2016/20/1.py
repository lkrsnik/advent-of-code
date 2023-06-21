import math

def solve1():
    max_value = 4294967295
    allowed = 0

    with open("input2", "r") as filestream:
        limits = []
        for line in filestream:
            limit = line.split('-')
            limits.append([int(limit[0]), int(limit[1])])

        
        i = 0
        while i < max_value:
            inLimits = False
            for l in limits:
                if l[0] <= i and l[1] >= i:
                    i = l[1]
                    inLimits = True
            if not inLimits:
                # PART 1
                # print i
                # break

                # PART 2
                allowed += 1
            i += 1
                
        print allowed


solve1()
