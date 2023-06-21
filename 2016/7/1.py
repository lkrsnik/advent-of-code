from collections import Counter

def solve1():
    result = 0
    with open("input", "r") as filestream:
        for line in filestream:
            # print range(len(line)-4)
            braclets = 0
            correct = False
            for i in range(len(line)-4):
                # print line[i:i+4]
                # print 'Start: ' + line[i] + ' End: ' + line[i+3]
                if line[i] == '[':
                    braclets += 1
                elif line [i] == ']':
                    braclets -= 1
                if line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
                    if braclets != 0:
                        # print braclets
                        correct = False
                        break
                    else:
                        correct = True

            # print correct
            if correct:
                result += 1

    print result
    

def solve2():
    result = 0
    with open("input", "r") as filestream:
        for line in filestream:
            ob = []
            ib = []
            braclets = 0
            for i in range(len(line)-3):
                if line[i] == '[':
                    braclets += 1
                elif line [i] == ']':
                    braclets -= 1
                if line[i] == line[i+2] and line[i+1] != line[i+2] and line[i+1] != ']' and line[i+1] != '[':
                    if braclets != 0:
                        ib.append(line[i:i+3])
                    else:
                        ob.append(line[i:i+3])

            score = False
            for i in ib:
                for o in ob:
                    if i[0] == o[1] and i[1] == o[0]:
                        result += 1
                        score = True
                        break
                if score:
                    break
                

    print result

solve1()
solve2()