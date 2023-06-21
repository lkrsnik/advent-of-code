positions = []
with open('input.txt') as fp:
# with open('input_test.txt') as fp:
    for line in fp:
        positions.append(line[1:-2].split(', '))

positions = [[int(cor.split('=')[1]) for cor in pos] for pos in positions]
velocities = [[0, 0, 0] for _ in positions]

for step in range(1000):
    velocities_delta = [[0, 0, 0] for _ in positions]


    for pos1_i, pos1 in enumerate(positions):
        for pos2_i, pos2 in enumerate(positions):
            if pos1_i != pos2_i:
                for i in range(len(pos1)):
                    if positions[pos1_i][i] < positions[pos2_i][i]:
                        velocities_delta[pos1_i][i] += 1
                    elif positions[pos1_i][i] > positions[pos2_i][i]:
                        velocities_delta[pos1_i][i] -= 1

    # positions += velocities_delta

    for i in range(len(positions)):
        for j in range(len(positions[0])):
            velocities[i][j] += velocities_delta[i][j]
            positions[i][j] += velocities[i][j]

pot = [sum(list(map(abs, par))) for par in positions]
kin = [sum(list(map(abs, par))) for par in velocities]
res = sum(map(lambda x: x[0] * x[1], zip(kin, pot)))

# part 1 10944
print(res)
