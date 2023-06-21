import copy, time, heapq, sys
sys.setrecursionlimit(2000)

class TreeNode:
    contains_array = []
    def __init__(self,x,y,number=None,left=None,right=None,up=None,down=None, distance=99999999):
        self.x = x
        self.y = y
        self.number = number
        self.leftNode = left
        self.rightNode = right
        self.upNode = up
        self.downNode = down
        self.distance = distance

    def contains(self, x, y):
        for el in self.contains_array:
            if el.x == x and el.y == y:
                return el
        return False

        # self.contains=[]
        # return self.containsNode(x,y)

    # def containsNode(self, x, y):
    #     contain = False
    #     for el in self.contains:
    #         print el
    #     test = [contain for el in self.contains if el is not None and x == el.x and y == el.y]
    #     print test
    #     if contain:
    #         return False
    #     elif self.x == x and self.y == y:
    #         return self
    #     else:
    #         return self.leftNode.containsNode(x,y) or self.upNode.containsNode(x,y) or self.rightNode.containsNode(x,y) or self.downNode.containsNode(x,y)

    def addNeighbourNodes(self, map):
        if (map[self.y][self.x+1] != '#'):
            el = self.contains(self.x+1, self.y)
            if not el:
                num = None
                if map[self.y][self.x+1] != '.':
                    num = map[self.y][self.x+1]
                n = TreeNode(self.x+1, self.y, number=num)
                self.contains_array.append(n)
                n.addNeighbourNodes(map)
                # print str(self.x+1) + ':' + str(self.y)
            else:
                n = el
            self.rightNode = n
            n.leftNode = self

        if (map[self.y][self.x-1] != '#'):
            el = self.contains(self.x-1, self.y)
            if not el:
                num = None
                if map[self.y][self.x - 1] != '.':
                    num = map[self.y][self.x - 1]
                n = TreeNode(self.x-1, self.y, number=num)
                self.contains_array.append(n)
                n.addNeighbourNodes(map)
                # print str(self.x - 1) + ':' + str(self.y)
            else:
                n = el
            self.leftNode = n
            n.rightNode = self


        if (map[self.y+1][self.x] != '#'):
            el = self.contains(self.x, self.y+1)
            if not el:
                num = None
                if map[self.y + 1][self.x] != '.':
                    num = map[self.y + 1][self.x]
                n = TreeNode(self.x, self.y+1, number=num)

                self.contains_array.append(n)

                n.addNeighbourNodes(map)
                # print str(self.x) + ':' + str(self.y + 1)
            else:
                n = el
            self.upNode = n
            n.downNode = self

        if (map[self.y-1][self.x] != '#'):
            el = self.contains(self.x, self.y-1)
            if not el:
                num = None
                if map[self.y - 1][self.x] != '.':
                    num = map[self.y - 1][self.x]
                n = TreeNode(self.x, self.y-1, number=num)

                self.contains_array.append(n)

                n.addNeighbourNodes(map)
                # print str(self.x) + ':' + str(self.y - 1)
            else:
                n = el
            self.downNode = n
            n.upNode = self


    def getDistance(self, i, j):
        start_node = None
        for el in self.contains_array:
            # print el.number
            # print str(i)
            # print el.number == str(i)
            if el.number is not None and el.number == str(i):
                start_node = el
                break

        for k in range(300):
            start_node.clearDistance()
            node = start_node.countDistance(j, 0, k)
            if node:
                # print k
                return k
        # start_node.clearDistance()
        # print start_node.countDistance(j, 0, 50)

        # print start_node
        #
        # print 'asd'


    def clearDistance(self):
        for el in self.contains_array:
            el.distance = 99999999


    def countDistance(self, goal, count, max_len):
        if self.distance < count:
            return False
        self.distance = count

        # print str(self.x) + ':' + str(self.y)

        if self == None:
            return False

        if self.number is not None and self.number == str(goal):
            return self

        if count == max_len:
            return False

        res = False
        if self.rightNode != None:
            res = self.rightNode.countDistance(goal, count+1, max_len) or res

        if self.leftNode != None:
            res = self.leftNode.countDistance(goal, count+1, max_len) or res

        if self.upNode != None:
            res = self.upNode.countDistance(goal, count+1, max_len) or res

        if self.downNode != None:
            res = self.downNode.countDistance(goal, count+1, max_len) or res
        return res


    def hasLeftNode(self):
        return self.leftNode

    def hasRightNode(self):
        return self.rightNode

    def isLeftNode(self):
        return self.parent and self.parent.leftNode == self

    def isRightNode(self):
        return self.parent and self.parent.rightNode == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightNode or self.leftNode)

    def hasAnyNoderen(self):
        return self.rightNode or self.leftNode

    def hasBothNoderen(self):
        return self.rightNode and self.leftNode

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftNode = lc
        self.rightNode = rc
        if self.hasLeftNode():
            self.leftNode.parent = self
        if self.hasRightNode():
            self.rightNode.parent = self

def calcInt(state):
    num = copy.copy(state[2:])
    num = [10*num[2*i] + num[2*i+1] for i in range(len(num)/2)]
    num.sort()
    num.append(state[0])
    return int(''.join(map(str,num)))

def compare(mytree, nstate):
    el = mytree[calcInt(nstate)]
    if el != None:
        return el[1]-1 + nstate[1]-1
    return -1

def solve1():
    m_string = []
    max_input = 7
    with open("input", "r") as filestream:
    # max_input = 4
    # with open("input2", "r") as filestream:
        [m_string.append(list(o[:-1])) for o in filestream]
        # for i in m_string:
        #     print i
        tree_structure = TreeNode(1, 1, number='0')
        tree_structure.contains_array.append(tree_structure)

        # form tree structure
        print "Creating tree structure..."
        tree_structure.addNeighbourNodes(m_string)

        # get distances
        print "Obtaining distances..."
        distances = [[-1] * (max_input+1)] * (max_input + 1)
        for i in range(max_input + 1):
            for j in range(max_input + 1):
                if i == j:
                    distances[i][j] = 0
                else:
                    distances[i][j] = tree_structure.getDistance(i, j)
                    print str(i) + ':' + str(j)
                    print distances[i][j]


        # createInitialTree(m_string)


def createInitialTree(m_string):
    print m_string[1][1]
    x = 1
    y = 1




solve1()