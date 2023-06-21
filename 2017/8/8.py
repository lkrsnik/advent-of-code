input = []
with open('input') as fp:
    for line in fp:
        input.append(line.split())

registers = {}
max_value = -1000000
for line in input:
    #print registers
    if line[0] not in registers:
        registers[line[0]] = 0
    if line[4] not in registers:
        registers[line[4]] = 0
    cond = False
    if (line[5] == '>' and registers[line[4]] > int(line[6])) or \
            (line[5] == '<' and registers[line[4]] < int(line[6])) or \
            (line[5] == '>=' and registers[line[4]] >= int(line[6])) or \
            (line[5] == '<=' and registers[line[4]] <= int(line[6])) or \
            (line[5] == '==' and registers[line[4]] == int(line[6])) or \
            (line[5] == '!=' and registers[line[4]] != int(line[6])):
        cond = True

    if cond:
        if line[1] == 'inc':
            registers[line[0]] += int(line[2])
        elif line[1] == 'dec':
            registers[line[0]] -= int(line[2])

        if max_value < registers[line[0]]:
            max_value = registers[line[0]]

#print registers
print max(registers.values())
print max_value
