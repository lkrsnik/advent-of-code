import copy


def read(path: str) -> str:
    with open(path, 'r') as fp:
        text = fp.read()
    return text

# input_path = 'input-example.txt'
input_path = 'input.txt'

text = read(input_path)
obstacles = set()
pos = ()
start_pos = ()
j, i = 0, 0
for j, row in enumerate(text.strip().split('\n')):
    for i, el in enumerate(row):
        if el == '#':
            obstacles.add((i, j))
        elif el == '^':
            pos = (i, j)
            start_pos = (i, j)



direction_order = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# p1
path = set()
turn_step = 0
# move
while 0 <= pos[0] <= i and 0 <= pos[1] <= j:
    direction = direction_order[turn_step % 4]
    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    # if 0 <= new_pos[0] <= i and 0 <= new_pos[0] <= j
    if new_pos in obstacles:
        turn_step += 1
    else:
        path.add(new_pos)
        pos = new_pos
print(len(path) - 1)

# p2

base_obstacles = copy.copy(obstacles)
# move
def sim(obs_position, start_pos):
    print(obs_position)
    pos = start_pos
    obstacles = copy.copy(base_obstacles)
    obstacles.add(obs_position)
    turn_step = 0
    path = {}
    while 0 <= pos[0] <= i and 0 <= pos[1] <= j:
        direction = direction_order[turn_step % 4]
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if new_pos in obstacles:
            turn_step += 1
        else:
            if new_pos not in path:
                path[new_pos] = set()
            if direction in path[new_pos]:
                return True
            path[new_pos].add(direction)
            pos = new_pos
    return False

obs_pos = 0
for p1 in range(i + 1):
    for p2 in range(j + 1):
        if (p1, p2) not in base_obstacles and (p1, p2) != start_pos and sim((p1, p2), start_pos):
            obs_pos += 1

print(obs_pos)
