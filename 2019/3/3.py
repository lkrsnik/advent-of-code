with open('input.txt') as fp:
    commands = []
    for line in fp:
        commands.append(line.split(','))

# commands = [['R8','U5','L5','D3'], ['U7','R6','D4','L4']]
# commands = ["R75,D30,R83,U83,L12,D49,R71,U7,L72".split(','),
#             "U62,R66,U55,R34,D71,R55,D58,R83".split(',')]
# commands = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(','),
#             "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',')]


# def get_occupied_territories(commands):
#     occupied = []
#     loc = [0, 0]
#     for command in commands:
#         move_length = int(command[1:])
#         if command[0] == 'R':
#             occupied += [(loc[0] + i, loc[1]) for i in range(1, move_length + 1)]
#             loc[0] += move_length
#         elif command[0] == 'L':
#             occupied += [(loc[0] - i, loc[1]) for i in range(1, move_length + 1)]
#             loc[0] -= move_length
#         elif command[0] == 'U':
#             occupied += [(loc[0], loc[1] + i) for i in range(1, move_length + 1)]
#             loc[1] += move_length
#         elif command[0] == 'D':
#             occupied += [(loc[0], loc[1] - i) for i in range(1, move_length + 1)]
#             loc[1] -= move_length
#     return occupied


def get_occupied_territories(commands):
    vertical = []
    horizontal = []
    loc = [0, 0]
    steps = 0
    for command in commands:
        move_length = int(command[1:])
        if command[0] == 'R':
            horizontal += [((loc[0], loc[1], steps), (loc[0] + move_length, loc[1]))]
            loc[0] += move_length
        elif command[0] == 'L':
            horizontal += [((loc[0] - move_length, loc[1]), (loc[0], loc[1], steps))]
            loc[0] -= move_length
        elif command[0] == 'U':
            vertical += [((loc[0], loc[1], steps), (loc[0], loc[1] + move_length))]
            loc[1] += move_length
        elif command[0] == 'D':
            vertical += [((loc[0], loc[1] - move_length), (loc[0], loc[1], steps))]
            loc[1] -= move_length
        steps += move_length
    return horizontal, vertical


horizontal, vertical = get_occupied_territories(commands[0])

loc = [0, 0]
possible_results = []
steps = 0
for command in commands[1]:
    move_length = int(command[1:])
    if command[0] == 'R':
        for limits in vertical:
            # if x of vertical between start/end of this move and
            if limits[0][0] >= loc[0] and limits[0][0] <= loc[0] + move_length and loc[1] >= limits[0][1] and loc[1] <= limits[1][1]:
                # this steps
                steps_combined = steps + (limits[0][0] - loc[0])
                # other steps
                if len(limits[0]) == 3:
                    steps_combined += limits[0][2] + (loc[1] - limits[0][1])
                else:
                    steps_combined += limits[1][2] + (limits[1][1] - loc[1])
                possible_results.append((limits[0][0], loc[1], steps_combined))

        # if two moves overlap horizontally
        for limits in horizontal:
            if limits[0][1] == loc[1]:
                start = max(limits[0][0], loc[0])
                end = min(limits[1][0], loc[0] + move_length)
                for i in range(start, end + 1):
                    possible_results.append((i, loc[1], 0))
        # horizontal += ((loc[0], loc[1]), (loc[0] + move_length, loc[1]))
        loc[0] += move_length
    elif command[0] == 'L':
        for limits in vertical:
            # if x of vertical between start/end of this move and
            if limits[0][0] >= loc[0] - move_length and limits[0][0] <= loc[0] and loc[1] >= limits[0][1] and loc[1] <= limits[1][1]:
                # this steps
                steps_combined = steps + (loc[0] - limits[0][0])
                # other steps
                if len(limits[0]) == 3:
                    steps_combined += limits[0][2] + (loc[1] - limits[0][1])
                else:
                    steps_combined += limits[1][2] + (limits[1][1] - loc[1])
                possible_results.append((limits[0][0], loc[1], steps_combined))

        for limits in horizontal:
            if limits[0][1] == loc[1]:
                start = max(limits[0][0], loc[0] - move_length)
                end = min(limits[1][0], loc[0])
                for i in range(start, end + 1):
                    possible_results.append((i, loc[1], 0))
        loc[0] -= move_length
    elif command[0] == 'U':
        for limits in horizontal:
            # if x of vertical between start/end of this move and
            if limits[0][1] >= loc[1] and limits[0][1] <= loc[1] + move_length and loc[0] >= limits[0][0] and loc[0] <= limits[1][0]:
                # this steps
                steps_combined = steps + (limits[0][1] - loc[1])
                # other steps
                if len(limits[0]) == 3:
                    steps_combined += limits[0][2] + (loc[0] - limits[0][0])
                else:
                    steps_combined += limits[1][2] + (limits[1][0] - loc[0])
                possible_results.append((loc[0], limits[0][1], steps_combined))

        for limits in vertical:
            if limits[0][0] == loc[0]:
                start = max(limits[0][1], loc[1])
                end = min(limits[1][1], loc[1] + move_length)
                for i in range(start, end + 1):
                    possible_results.append((loc[0], i, 0))
        # vertical += ((loc[0], loc[1]), (loc[0], loc[1] + move_length))
        loc[1] += move_length
    elif command[0] == 'D':
        for limits in horizontal:
            # if x of vertical between start/end of this move and
            if limits[0][1] >= loc[1] - move_length and limits[0][1] <= loc[1] and loc[0] >= limits[0][0] and loc[0] <= limits[1][0]:
                # this steps
                steps_combined = steps + (loc[1] - limits[0][1])
                # other steps
                if len(limits[0]) == 3:
                    steps_combined += limits[0][2] + (loc[0] - limits[0][0])
                else:
                    steps_combined += limits[1][2] + (limits[1][0] - loc[0])
                possible_results.append((loc[0], limits[0][1], steps_combined))

        for limits in vertical:
            if limits[0][0] == loc[0]:
                start = max(limits[0][1], loc[1] - move_length)
                end = min(limits[1][1], loc[1])
                for i in range(start, end + 1):
                    possible_results.append((loc[0], i, 0))
        loc[1] -= move_length
    steps += move_length

wire2 = get_occupied_territories(commands[1])


# for el in wire1:
#     if el in wire2:
#         possible_results.append(el)

min_len = 100000000
min_el = ()
min_steps = 100000000
for el in possible_results:
    res = abs(el[0]) + abs(el[1])
    if res < min_len and res != 0:
        min_len = res
        min_el = el
    if el[2] < min_steps and el[2] != 0:
        min_steps = el[2]
        # min_el = el


# part 1 721
# print(min_el)
print(min_len)

# part 2 7388
print(min_steps)
