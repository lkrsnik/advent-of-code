input = []
with open('input') as fp:
    for line in fp:
        input.append(map(int, line.replace(':', '').split()))

# print input

step = 10
#loc = 0
severity = 0
j = 0
while True:
    init_step = j
    # init_step = 10
    step = init_step
    caught = False
    for i in range(len(input)):
        # if (0 == step % input[i][1] and step/input[i][1] % 2 == 0) or ( == step % input[i][1] and step/input[i][1] % 2 == 0):
        test = step % ((input[i][1] - 1) * 2)
        if 0 == step % ((input[i][1] - 1) * 2):
            # severity += input[i][0] * input[i][1]
            caught = True

        if len(input) > i + 1:
            step = init_step + input[i + 1][0]
    if not caught:
        break
    j += 1

# too low: 129778

# print severity
print j
