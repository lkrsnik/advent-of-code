# input = []

def calculate_output(input_val):
    with open('input.txt') as fp:
        for line in fp:
            input = line.split(',')
            commands = [int(a) for a in input]

    # commands[1] = com1
    # commands[2] = com2
    # commands = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,
    # 1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    i = 0
    res = -1
    while i < len(input):
        opcode = commands[i] % 100
        par1 = int(commands[i] / 100) % 10
        par2 = int(commands[i] / 1000) % 10
        par3 = int(commands[i] / 10000) % 10
        if par3:
            print("ERROR!?!")

        # handle command
        if opcode == 1:
            p1 = commands[i+1] if par1 else commands[commands[i+1]]
            p2 = commands[i+2] if par2 else commands[commands[i+2]]

            commands[commands[i+3]] = p1 + p2
            i += 4
        elif opcode == 2:
            p1 = commands[i + 1] if par1 else commands[commands[i + 1]]
            p2 = commands[i + 2] if par2 else commands[commands[i + 2]]

            commands[commands[i+3]] = p1 * p2
            i += 4
        elif opcode == 3:
            if par1 or par2:
                print('ERROR!')

            commands[commands[i+1]] = input_val
            i += 2
        elif opcode == 4:
            if par1:
                # print(commands[i + 1])
                res = commands[i + 1]
            else:
                # print(commands[commands[i+1]])
                res = commands[commands[i+1]]
            i += 2

        elif opcode == 5:
            p1 = commands[i + 1] if par1 else commands[commands[i + 1]]
            p2 = commands[i + 2] if par2 else commands[commands[i + 2]]
            # p3 = commands[i + 3] if par3 else commands[commands[i + 3]]

            if p1:
                i = p2
            else:
                i += 3
        elif opcode == 6:
            p1 = commands[i + 1] if par1 else commands[commands[i + 1]]
            p2 = commands[i + 2] if par2 else commands[commands[i + 2]]
            # p3 = commands[i + 3] if par3 else commands[commands[i + 3]]

            if not p1:
                i = p2
            else:
                i += 3
        elif opcode == 7:
            p1 = commands[i + 1] if par1 else commands[commands[i + 1]]
            p2 = commands[i + 2] if par2 else commands[commands[i + 2]]
            # p3 = commands[i + 3] if par3 else commands[commands[i + 3]]

            if p1 < p2:
                store_value = 1
            else:
                store_value = 0
            if par3:
                commands[i + 3] = store_value
            else:
                commands[commands[i + 3]] = store_value
            i += 4
        elif opcode == 8:
            p1 = commands[i + 1] if par1 else commands[commands[i + 1]]
            p2 = commands[i + 2] if par2 else commands[commands[i + 2]]
            # p3 = commands[i + 3] if par3 else commands[commands[i + 3]]

            if p1 == p2:
                store_value = 1
            else:
                store_value = 0
            if par3:
                commands[i + 3] = store_value
            else:
                commands[commands[i + 3]] = store_value
            i += 4
        elif opcode == 99:
            break

    return res

# part 1 13547311
print(calculate_output(1))

# part 2 236453
print(calculate_output(5))


# print()

# f_i = -1
# f_j = -1
# res = False
# for i in range(100):
#     for j in range(100):
#         if calculate_output(i, j) == 19690720:
#             res = True
#             f_i = i
#             f_j = j
#             break
#     if res:
#         break
#
# # result
# print(100 * f_i + f_j)
