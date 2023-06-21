import re

input = []
with open('input') as fp:
    for line in fp:
        input.append(re.split('[ \n#,:x]', line))

actual_input = [[int(i[1]), int(i[3]), int(i[4]), int(i[6]), int(i[7])]for i in input]

# max_x, max_y =

matrix = [list("." * 1200) for _ in range(1200)]

for inp in actual_input:
    for i in range(inp[1], inp[1]+inp[3]):
        for j in range(inp[2], inp[2] + inp[4]):
            if matrix[i][j] == ".":
                matrix[i][j] = inp[0]
                # matrix[i][j] = "o"
            else:
                matrix[i][j] = "X"

res = 0
for i in range(1200):
    for j in range(1200):
        if matrix[i][j] == 'X':
            res += 1

print(res)


for inp in actual_input:
    pure = True
    for i in range(inp[1], inp[1]+inp[3]):
        for j in range(inp[2], inp[2] + inp[4]):
            if matrix[i][j] == "X":
                pure = False
    if pure:
        print(inp[0])
        break
