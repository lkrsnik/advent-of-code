from collections import Counter

def solve1():
    result = 0
    with open("input", "r") as filestream:
        for line in filestream:
            currentline = line.split("-")
            if currentline[-1][:-1].split('[')[1][:-1] == ''.join(list(zip(*sorted(Counter(''.join(currentline[:-1])).most_common(), key=lambda (x,y): (-y,x))[:5]))[0]):
                result += int(currentline[-1][:-1].split('[')[0])

        print result

def solve2():
    with open("input", "r") as filestream:
        for line in filestream:
            currentline = line.split("-")
            if currentline[-1][:-1].split('[')[1][:-1] == ''.join(list(zip(*sorted(Counter(''.join(currentline[:-1])).most_common(), key=lambda (x,y): (-y,x))[:5]))[0]):
                result = ''
                for c in ' '.join(line.split("-")[:-1]):
                    if c == ' ':
                        result += ' '
                        continue

                    result += chr(((ord(c) - ord('a') + int(currentline[-1][:-1].split('[')[0])) % 26) + ord('a'))
                print result, int(currentline[-1][:-1].split('[')[0])


solve1()
solve2()