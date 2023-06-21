from collections import Counter

input = []
with open('input') as fp:
    for line in fp:
        input.append(int(line))



loc = 0
steps = 0

while loc < len(input) and loc >= 0:
    input[loc] += 1
    loc = loc + input[loc] - 1
    steps += 1


print steps



input = []
with open('input') as fp:
    for line in fp:
        input.append(int(line))



loc = 0
steps = 0

while loc < len(input) and loc >= 0:
    if input[loc] < 3:
        input[loc] += 1
        loc = loc + input[loc] - 1
    else:
        input[loc] += -1
        loc = loc + input[loc] + 1
    steps += 1


print steps