import copy, time, heapq

class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def spliceOut(self):
       if self.isLeaf():
           if self.isLeftChild():
                  self.parent.leftChild = None
           else:
                  self.parent.rightChild = None
       elif self.hasAnyChildren():
           if self.hasLeftChild():
                  if self.isLeftChild():
                     self.parent.leftChild = self.leftChild
                  else:
                     self.parent.rightChild = self.leftChild
                  self.leftChild.parent = self.parent
           else:
                  if self.isLeftChild():
                     self.parent.leftChild = self.rightChild
                  else:
                     self.parent.rightChild = self.rightChild
                  self.rightChild.parent = self.parent

    def findSuccessor(self):
      succ = None
      if self.hasRightChild():
          succ = self.rightChild.findMin()
      else:
          if self.parent:
                 if self.isLeftChild():
                     succ = self.parent
                 else:
                     self.parent.rightChild = None
                     succ = self.parent.findSuccessor()
                     self.parent.rightChild = self
      return succ

    def findMin(self):
      current = self
      while current.hasLeftChild():
          current = current.leftChild
      return current

    def remove(self,currentNode):
         if currentNode.isLeaf(): #leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): #interior
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # this node has one child
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

def validateState(mytree, ninputs, nstate, states):
    for i in range(ninputs):
        if i % 2 == 1 and nstate[2 + i] != nstate[1 + i]:
            for j in range(ninputs):
                if j % 2 == 0 and nstate[2 + i] == nstate[2 + j]:
                    return False
    if mytree[calcInt(nstate)] == None:
        return True
    return False

def isTop(ninputs, nstate):
    for i in range(ninputs):
        if nstate[i + 2] != 4:
            return False
    return True

def calcNextObject(res, btree, isforward, mytree, allTop, state, ninputs, states, nstates, dif):
    nstate = copy.copy(state)
    nstate[0] = state[0] + dif
    nstate[1] = state[1] + 1
    start_time = time.time()

    for i in range(ninputs):
        if state[2 + i] == state[0]:
            nnstate = copy.copy(nstate)
            nnstate[2 + i] += dif
            if validateState(mytree, ninputs, nnstate, states):
                if (isforward and compare(btree, nnstate)!= -1):
                    allTop = True
                    res = compare(btree, nnstate)
                mytree[calcInt(nnstate)] = nnstate
                nstates.append(nnstate)
            for j in range(i + 1, ninputs):
                # if object in same layer
                if state[2 + j] == state[0]:
                    nnnstate = copy.copy(nnstate)
                    nnnstate[2 + j] += dif
                    if validateState(mytree, ninputs, nnnstate, states):
                        if (isforward and compare(btree, nnnstate) != -1):
                            allTop = True
                            res = compare(btree, nnnstate)

                        mytree[calcInt(nnnstate)] = nnnstate
                        nstates.append(nnnstate)

    return nstates, allTop, res

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
    ninputs = 14
    result = 1
    res = 0
    with open("input3", "r") as filestream:
        for line in filestream:
            initial = [1, 1]
            binitial = [4, 1]
            initiall = line.split()
            binitiall = [4] * len(initiall)
            [binitial.append(int(s)) for s in binitiall]
            [initial.append(int(s)) for s in initiall]
            mytree = BinarySearchTree()
            mytree[calcInt(initial)] = initial
            btree = BinarySearchTree()
            btree[calcInt(binitial)] = binitial
            states = [initial]
            pstates = [initial]
            bstates = [binitial]
            bpstates = [binitial]
            allTop = False
            while(not allTop):
                result += 1
                print result - 1
                nstates = [[]]
                for state in pstates:
                    # a layer higher
                    if state[0] + 1 <= ninputs:
                        nstates, allTop, res = calcNextObject(res, btree, True, mytree, allTop, state, ninputs, states, nstates, 1)

                    # a layer lower
                    if state[0] - 1 > 0:
                        nstates, allTop, res = calcNextObject(res, btree, True, mytree, allTop, state, ninputs, states, nstates, -1)
                pstates = nstates[1:]
                states.extend(nstates[1:])
                result += 1
                print result - 1
                bnstates = [[]]
                for bstate in bpstates:
                    # a layer higher
                    if bstate[0] + 1 <= ninputs:
                        bnstates, allTop, res = calcNextObject(res, [], False, btree, allTop, bstate, ninputs, bstates, bnstates, 1)
                    # a layer lower
                    if bstate[0] - 1 > 0:
                        bnstates, allTop, res = calcNextObject(res, [], False, btree, allTop, bstate, ninputs, bstates, bnstates, -1)

                bpstates = bnstates[1:]
                bstates.extend(bnstates[1:])
    print res

solve1()