import copy

def calcCoor(x, y, n):
    # print x*x + 3*x + 2*x*y + y + y*y
    # print "{0:b}".format(x*x + 3*x + 2*x*y + y + y*y)
    # print [int(el) for el in "{0:b}".format(x*x + 3*x + 2*x*y + y + y*y)]
    return sum([int(el) for el in "{0:b}".format(x*x + 3*x + 2*x*y + y + y*y + n)])%2

def isNotPrev(pLocations,loc):
    for ploc in pLocations:
        if ploc == []:
            continue
        if ploc[0] == loc[0] and ploc[1] == loc[1]:
            return False
    return True

def solve1():
    # number = 10
    # finalLoc = [7,4]

    number = 1350
    finalLoc = [31,39]


    print calcCoor(9, 5, number)

    locations = [[],[1,1]]
    depth = 0
    elFound = False

    while not elFound:
        nLocations = [[]]
        for loc in locations:
            if loc == []:
                continue
            if loc[0] == finalLoc[0] and loc[1] == finalLoc[1]:
                elFound = True
            # x + 1
            if calcCoor(loc[0]+1, loc[1], number) == 0 and isNotPrev(locations,[loc[0]+1, loc[1]]):
                nLocations.append([loc[0]+1, loc[1]])
            if calcCoor(loc[0], loc[1]+1, number) == 0 and isNotPrev(locations,[loc[0], loc[1]+1]):
                nLocations.append([loc[0], loc[1]+1])
            if loc[0]-1 >= 0 and calcCoor(loc[0]-1, loc[1], number) == 0 and isNotPrev(locations,[loc[0]-1, loc[1]]):
                nLocations.append([loc[0]-1, loc[1]])
            if loc[1]-1 >= 0 and calcCoor(loc[0], loc[1]-1, number) == 0 and isNotPrev(locations,[loc[0], loc[1]-1]):
                nLocations.append([loc[0], loc[1]-1])
        locations.extend(nLocations)
        depth += 1

    print depth - 1

def solve2():
    number = 10
    maxStep = 5

    number = 1350
    maxStep = 50

    locations = [[1,1]]
    depth = 0

    while depth < maxStep:
        print depth
        for loc in copy.deepcopy(locations):
            if loc == []:
                continue
            # x + 1
            if calcCoor(loc[0]+1, loc[1], number) == 0 and isNotPrev(locations,[loc[0]+1, loc[1]]):
                locations.append([loc[0]+1, loc[1]])
            if calcCoor(loc[0], loc[1]+1, number) == 0 and isNotPrev(locations,[loc[0], loc[1]+1]):
                locations.append([loc[0], loc[1]+1])
            if loc[0]-1 >= 0 and calcCoor(loc[0]-1, loc[1], number) == 0 and isNotPrev(locations,[loc[0]-1, loc[1]]):
                locations.append([loc[0]-1, loc[1]])
            if loc[1]-1 >= 0 and calcCoor(loc[0], loc[1]-1, number) == 0 and isNotPrev(locations,[loc[0], loc[1]-1]):
                locations.append([loc[0], loc[1]-1])
        depth += 1

    print len(locations)
    print locations

# solve1()
solve2()