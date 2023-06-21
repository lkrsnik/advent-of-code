input = []
with open('input') as fp:
    for line in fp:
        input.append(map(int, line.split()))

print(sum([max(line)-min(line) for line in input]))

print(sum([sum([sum([el1/el2 for el2 in line if el1 % el2 == 0 and el1 != el2]) for el1 in line]) for line in input]))
