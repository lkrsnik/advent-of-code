# input = []
import copy
import itertools


class Amplifier(object):
    def __init__(self, commands):
        self.commands = copy.copy(commands)
        self.use_phase_settings = True
        # self.input_val = input_val
    def calculate_output(self, phase_setting_val, input_val):
        # input_val = yield
        i = 0
        res = -1
        while i < len(input):
            opcode = self.commands[i] % 100
            par1 = int(self.commands[i] / 100) % 10
            par2 = int(self.commands[i] / 1000) % 10
            par3 = int(self.commands[i] / 10000) % 10
            if par3:
                print("ERROR!?!")

            # handle command
            if opcode == 1:
                p1 = self.commands[i+1] if par1 else self.commands[self.commands[i+1]]
                p2 = self.commands[i+2] if par2 else self.commands[self.commands[i+2]]

                self.commands[self.commands[i+3]] = p1 + p2
                i += 4
            elif opcode == 2:
                p1 = self.commands[i + 1] if par1 else self.commands[self.commands[i + 1]]
                p2 = self.commands[i + 2] if par2 else self.commands[self.commands[i + 2]]

                self.commands[self.commands[i+3]] = p1 * p2
                i += 4
            elif opcode == 3:
                if par1 or par2:
                    print('ERROR!')
                if self.use_phase_settings:
                    self.commands[self.commands[i + 1]] = phase_setting_val
                    self.use_phase_settings = False
                else:
                    self.commands[self.commands[i+1]] = input_val
                i += 2
            elif opcode == 4:
                if par1:
                    # print(commands[i + 1])
                    res = self.commands[i + 1]
                else:
                    # print(commands[commands[i+1]])
                    res = self.commands[self.commands[i+1]]
                i += 2
                input_val = yield res
                # return res

            elif opcode == 5:
                p1 = self.commands[i + 1] if par1 else self.commands[self.commands[i + 1]]
                p2 = self.commands[i + 2] if par2 else self.commands[self.commands[i + 2]]
                # p3 = commands[i + 3] if par3 else commands[commands[i + 3]]

                if p1:
                    i = p2
                else:
                    i += 3
            elif opcode == 6:
                p1 = self.commands[i + 1] if par1 else self.commands[self.commands[i + 1]]
                p2 = self.commands[i + 2] if par2 else self.commands[self.commands[i + 2]]
                # p3 = commands[i + 3] if par3 else commands[commands[i + 3]]

                if not p1:
                    i = p2
                else:
                    i += 3
            elif opcode == 7:
                p1 = self.commands[i + 1] if par1 else self.commands[self.commands[i + 1]]
                p2 = self.commands[i + 2] if par2 else self.commands[self.commands[i + 2]]
                # p3 = commands[i + 3] if par3 else commands[commands[i + 3]]

                if p1 < p2:
                    store_value = 1
                else:
                    store_value = 0
                if par3:
                    self.commands[i + 3] = store_value
                else:
                    self.commands[self.commands[i + 3]] = store_value
                i += 4
            elif opcode == 8:
                p1 = self.commands[i + 1] if par1 else self.commands[self.commands[i + 1]]
                p2 = self.commands[i + 2] if par2 else self.commands[self.commands[i + 2]]
                # p3 = commands[i + 3] if par3 else commands[commands[i + 3]]

                if p1 == p2:
                    store_value = 1
                else:
                    store_value = 0
                if par3:
                    self.commands[i + 3] = store_value
                else:
                    self.commands[self.commands[i + 3]] = store_value
                i += 4
            elif opcode == 99:
                yield -1
            else:
                print('ERROR!!!')

        return -1

with open('input.txt') as fp:
    for line in fp:
        input = line.split(',')
        all_commands = [int(a) for a in input]

# # settings = [4,3,2,1,0]
# options = [0, 1, 2, 3, 4]
#
#
# # all_commands = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
# # 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
#
# best_res = -1
# res_phase_settings = None
# for settings in itertools.permutations(options, 5):
#     previous_amp_output = 0
#     for setting in settings:
#         amp = Amplifier(all_commands)
#         previous_amp_output = amp.calculate_output(setting, previous_amp_output)
#         # previous_amp_output = amp.calculate_output(previous_amp_output)
#
#     if best_res < previous_amp_output:
#         res_phase_settings = settings
#         best_res = previous_amp_output
#
# # part 1 - 20413
# print(res_phase_settings)
# print(best_res)
#
options = [5, 6, 7, 8, 9]

# all_commands = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
# 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# all_commands = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

best_res = -1
res_phase_settings = None
for settings in itertools.permutations(options, 5):
    # create generators
    generators = []
    output = 0
    for setting in settings:
        amp = Amplifier(all_commands)
        generators.append(amp.calculate_output(setting, output))
        output = next(generators[-1])
    previous_amp_output = output
    while(True):
        for gen in generators:
            output = gen.send(output)
            # output = next(gen)
            if output == -1:
                break
        if output == -1:
            break
        previous_amp_output = output

    if best_res < previous_amp_output:
        res_phase_settings = settings
        best_res = previous_amp_output

# part 2 - 3321777
print(res_phase_settings)
print(best_res)
