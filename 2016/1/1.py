def solve():
    x = 0
    y = 0
    d = 0
    xfin = -1
    yfin = -1
    locations = []
    with open("input", "r") as filestream:
        for line in filestream:
            currentline = line.split(", ")
            for el in currentline:
                
                d = curveDirection(d, el[0])
                #print "HEREEEEEE", d, el
                for e in locations:
                    #print e
                    if (e[0] == x and e[1] == y and xfin == -1 and yfin == -1):
                    	#print "HERE"
                        xfin = x
                        yfin = y
                nx, ny = calculate(d, int(el[1:]), x, y)
                #print 'RANGE1', x, nx
                move = 1
                if (nx < x):
                    move = -1
                for i in range(x, nx, move):
                    #print i, y
                    for e in locations:
                    #print e
                        if (e[0] == i and e[1] == y and xfin == -1 and yfin == -1):
                        #print "HERE"
                            xfin = i
                            yfin = y
                    locations.append([i,y])

                #print 'RANGE2', y, ny
                move = 1
                if (ny < y):
                    move = -1
                for i in range(y, ny, move):
                    #print x, i
                    for e in locations:
                        #print e
                        if (e[0] == x and e[1] == i and xfin == -1 and yfin == -1):
                        #print "HERE"
                            xfin = x
                            yfin = i
                    locations.append([x,i])
            	locations.append([x,y])
                x, y = nx, ny
                #print 'NEW X', nx, ny
            print abs(x) + abs(y)
            print abs(xfin) + abs(yfin)

def curveDirection(currD, curve):
    if (curve == "R"):
    	currD += 1
    else:
    	currD -= 1
    return currD % 4

def calculate(currD, number, x, y):
    if (currD == 0):
        y += number
    elif (currD == 1):
        x += number
    elif (currD == 2):
        y -= number
    else:
        x -= number
    return x, y

    #print y, x
solve()