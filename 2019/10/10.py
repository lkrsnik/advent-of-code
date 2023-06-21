import copy
from math import gcd

asteroid_map = []
with open('input.txt') as fp:
# with open('input_test.txt') as fp:
    for line in fp:
        asteroid_map.append(list(line.split()[0]))


def get_vision(m_x, m_y, asteroid_map):
    asteroid_map[m_y][m_x] = 'o'
    for y in range(len(asteroid_map)):
        for x in range(len(asteroid_map[0])):
            if asteroid_map[y][x] == '#':
                distance_x = x - m_x
                distance_y = y - m_y
                gcd_res = gcd(distance_x, distance_y)
                move_x = distance_x // gcd_res
                move_y = distance_y // gcd_res
                i = 1
                while x + move_x * i >= 0 and x + move_x * i < len(asteroid_map[0]) and y + move_y * i >= 0 and y + move_y * i < len(asteroid_map):
                    asteroid_map[y + move_y * i][x + move_x * i] = 'o'
                    i += 1

    see_num = 0
    for row in asteroid_map:
        for el in row:
            if el == '#':
                see_num += 1
    return see_num

vision_asteroid_map = copy.deepcopy(asteroid_map)
# asteroids
max_vision = -1
max_pos = []
for m_y in range(len(asteroid_map)):
    for m_x in range(len(asteroid_map[0])):
        if asteroid_map[m_y][m_x] == '#':
            res = get_vision(m_x, m_y, copy.deepcopy(asteroid_map))
            vision_asteroid_map[m_y][m_x] = res
            if res > max_vision:
                max_vision = res
                max_pos=[m_x, m_y]
            # print('here')

print(max_vision)

print(gcd(-3, 0))

print('here')