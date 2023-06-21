from collections import Counter
import time
import itertools


def solve1():
    nodes = []
    j=0
    with open("input", "r") as filestream:
        [nodes.append(o[:-1]) for o in filestream]
        i = 0
        coor = ['1'*34]*30
        print coor
        for i in range(len(nodes)):
            node = nodes[i].split()

            # print node[2][:-1]
            # print int(node[2][:-1])
            # print orders
            if int(node[2][:-1])<=89:
                j += 1
            
            # print word

    print j
    # print word


def solve2():
    nodes = []
    j=0
    with open("input", "r") as filestream:
        [nodes.append(o[:-1]) for o in filestream]
        i = 0
        coor = [['0' for x in range(34)] for y in range(30)] 
        # coor = ['a'*34]*30
        print coor
        for i in range(len(nodes)):
            node = nodes[i].split()


            v = int(node[2][:-1])
            loc = [i%30,i/30]
            if int(node[2][:-1])<=1:
                print 'HERE'
                print loc[0], loc[1]
                coor[loc[0]][loc[1]] = '_'
            elif int(node[2][:-1])<=89:
                coor[loc[0]][loc[1]] = '.'
            else:
                coor[loc[0]][loc[1]] = '#'

        img = ''
        for y in coor:
            for x in y:
                img += x
            img += '\n'
        print img
    print j


# solve1()
solve2()

# 180