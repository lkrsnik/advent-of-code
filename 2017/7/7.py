input = []
with open('input') as fp:
    for line in fp:
        input.append(line.split())

potentials = []
for line in input:
    if len(line) > 2:
        potentials.append(line[0])

for line in input:
    if len(line) > 2:
        for el in line[3:]:
            if el[-1] == ',':
                el = el[:-1]
            if el in potentials:
                potentials.remove(el)

print potentials[0]

weights = {}
for line in input:
    sons = []
    if len(line) > 2:
        for el in line[3:]:
            if el[-1] == ',':
                el = el[:-1]
            sons.append(el)
    weights[line[0]] = {'weight': int(line[1][1:-1]), 'sons': sons}

def recursion(name):
    sum = weights[name]['weight']
    w = -1
    message = name + ' --> '
    p = False
    for el in weights[name]['sons']:
        rec = recursion(el)
        message += el + ': ' + str(rec) + ', '
        if w == -1:
            w = rec
        if w != rec:
            p = True
        sum += rec
    if p:
        print message
    return sum
    # if weights[name]
    # weights[name]

recursion(potentials[0])