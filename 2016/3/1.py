def solve1():
    result = 0
    with open("input", "r") as filestream:
        for line in filestream:
            triangle = line.split()
            # print (sum(map(int, triangle)))
            # print (max(map(int, triangle)))
            if (sum(map(int, triangle)) - (2 * max(map(int, triangle))) > 0):
                result += 1
        print result

def solve2():
    result = 0
    linen = 0
    with open("input", "r") as filestream:
        triangleset =[[0,0,0]]
        for line in filestream:
            triangleset.append(line.split())
            if (linen % 3 == 2):
                if (sum(map(int, list(list(zip(*triangleset))[0][1:]))) - (2 * max(map(int, list(list(zip(*triangleset))[0][1:])))) > 0):
                    result += 1
                if (sum(map(int, list(list(zip(*triangleset))[1][1:]))) - (2 * max(map(int, list(list(zip(*triangleset))[1][1:])))) > 0):
                    result += 1
                if (sum(map(int, list(list(zip(*triangleset))[2][1:]))) - (2 * max(map(int, list(list(zip(*triangleset))[2][1:])))) > 0):
                    result += 1
                triangleset =[[0,0,0]]

            linen += 1
        print result

solve1()
solve2()