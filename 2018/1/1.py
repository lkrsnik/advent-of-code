input = []
with open('input') as fp:
    for line in fp:
        input.append(int(line.split()[0]))

r = 0
l = set()
free_set = True
while free_set:
    for i in input:
        l.add(r)
        r += i
        if r in l:
            print(r)
            free_set = False
            break


# print(r)
