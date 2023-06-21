import fileinput

for line in fileinput.input():
    print(sum([map(int, list(line)[:-1])[i] for i in range(len(map(int, list(line)[:-1]))) if
               map(int, list(line)[:-1])[i] == map(int, list(line)[:-1])[(i+1)%len(map(int, list(line)[:-1]))]]))

    print(sum([map(int, list(line)[:-1])[i] for i in range(len(map(int, list(line)[:-1]))) if
               map(int, list(line)[:-1])[i] == map(int, list(line)[:-1])[(i + (len(map(int, list(line)[:-1]))/2)) % len(map(int, list(line)[:-1]))]]))
