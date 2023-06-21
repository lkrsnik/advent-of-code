# input = []

def calculate_output(com1, com2):
    with open('input.txt') as fp:
        for line in fp:
            input = line.split(',')
            commands = [int(a) for a in input]

    commands[1] = com1
    commands[2] = com2

    # commands = [1,1,1,4,99,5,6,0,99]
    i = 0
    while i < len(input):
        # handle command
        if commands[i] == 1:
            commands[commands[i+3]] = commands[commands[i+1]] + commands[commands[i+2]]
        if commands[i] == 2:
            commands[commands[i+3]] = commands[commands[i+1]] * commands[commands[i+2]]
        if commands[i] == 99:
            break
        i += 4
    return commands[0]

# part 1
# 6568671
print(calculate_output(12, 2))

# part 2
f_i = -1
f_j = -1
res = False
for i in range(100):
    for j in range(100):
        if calculate_output(i, j) == 19690720:
            res = True
            f_i = i
            f_j = j
            break
    if res:
        break

# result
print(100 * f_i + f_j)
