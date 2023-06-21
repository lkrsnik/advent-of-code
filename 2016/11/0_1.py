import copy, time



def validateState(ninputs, nstate, states):
    for i in range(ninputs):
        if i % 2 == 1 and nstate[2 + i] != nstate[1 + i]:
            for j in range(ninputs):
                if j % 2 == 0 and nstate[2 + i] == nstate[2 + j]:
                    return False

    for state in states:
        equal = True
        if state[0] != nstate[0]:
            equal = False
        for i in range(ninputs):
            if state[i + 2] != nstate[i + 2]:
                equal = False
        if equal:
            return False

    #     if state[0] == nstate[0]
    return True

def isTop(ninputs, nstate):
    for i in range(ninputs):
        if nstate[i + 2] != 4:
            return False
    return True

def calcNextObject(allTop, state, ninputs, states, nstates, dif):
    nstate = copy.copy(state)
    nstate[0] = state[0] + dif
    nstate[1] = state[1] + 1

    # print len(states)
    start_time = time.time()

    for i in range(ninputs):
        # if object in same layer
        if state[2 + i] == state[0]:
            nnstate = copy.copy(nstate)
            nnstate[2 + i] += dif
            # print 'PREVAL'
            # print time.time() - start_time
            if validateState(ninputs, nnstate, states):
                if isTop(ninputs, nnstate):
                    print nnstate[1] - 1
                    allTop = True
                nstates.append(nnstate)
            # print 'AFTVAL'
            # print time.time() - start_time
            for j in range(i + 1, ninputs):
                # if object in same layer
                if state[2 + j] == state[0]:
                    nnnstate = copy.copy(nnstate)
                    nnnstate[2 + j] += dif
                    if validateState(ninputs, nnnstate, states):
                        if isTop(ninputs, nnnstate):
                            print nnnstate[1] - 1
                            allTop = True
                        nstates.append(nnnstate)

    return nstates, allTop

def calcInt(state):
    num = copy.copy(state[2:])
    num.append(state[0])
    return int(''.join(map(str,num)))

def solve1():
    ninputs = 10
    result = 1
    with open("input2", "r") as filestream:
        for line in filestream:
            binitial = [1, 1]
            initial = line.split()
            [binitial.append(int(s)) for s in initial]

            # binitial.append(int(''.join(map(str,binitial[0].extend(binitial[2:])))))
            print calcInt(binitial)
            

            states = [binitial]
            pstates = [binitial]


            allTop = False
            while(not allTop):
                result += 1
                print result - 1
                nstates = [[]]
                for state in pstates:
                    # a layer higher
                    if state[0] + 1 <= ninputs:
                        nstates, allTop = calcNextObject(allTop, state, ninputs, states, nstates, 1)

                    # a layer lower
                    if state[0] - 1 > 0:
                        nstates, allTop = calcNextObject(allTop, state, ninputs, states, nstates, -1)

                pstates = nstates[1:]
                states.extend(nstates[1:])

    print result - 1

solve1()