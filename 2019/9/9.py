# input = []
import copy
import itertools


class Amplifier(object):
    def __init__(self, commands, phase_settings):
        self.commands = copy.copy(commands)
        self.use_phase_settings = phase_settings
        self.relative_base = 0
        # self.input_val = input_val

    def get_mode_value(self, ind, parameter):
        if parameter == 0:
            final_index = self.commands[ind]
        elif parameter == 1:
            final_index = ind
        elif parameter == 2:
            final_index = self.commands[ind] + self.relative_base
        if final_index not in self.commands:
            self.commands[final_index] = 0
        return self.commands[final_index]
        # return self.commands[ind] if parameter else self.commands[self.commands[ind]]

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
                p1 = self.get_mode_value(i + 1, par1)
                p2 = self.get_mode_value(i + 2, par2)

                self.commands[self.commands[i+3]] = p1 + p2
                i += 4
            elif opcode == 2:
                p1 = self.get_mode_value(i + 1, par1)
                p2 = self.get_mode_value(i + 2, par2)

                self.commands[self.commands[i+3]] = p1 * p2
                i += 4
            elif opcode == 3:
                # if par1 or par2:
                #     print('ERROR!')
                if self.use_phase_settings:
                    if par1 == 0:
                        final_index = self.commands[i + 1]
                    elif par1 == 1:
                        final_index = i + 1
                    elif par1 == 2:
                        final_index = self.commands[i + 1] + self.relative_base
                    # if final_index not in self.commands:
                    self.commands[final_index] = phase_setting_val
                    self.use_phase_settings = False
                else:
                    if par1 == 0:
                        final_index = self.commands[i + 1]
                    elif par1 == 1:
                        final_index = i + 1
                    elif par1 == 2:
                        final_index = self.commands[i + 1] + self.relative_base
                    # if final_index not in self.commands:
                    self.commands[final_index] = input_val
                    # self.commands[self.commands[i+1]] = input_val
                i += 2
            elif opcode == 4:
                p1 = self.get_mode_value(i + 1, par1)
                i += 2
                input_val = yield p1
                # return res

            elif opcode == 5:
                p1 = self.get_mode_value(i + 1, par1)
                p2 = self.get_mode_value(i + 2, par2)
                # p3 = commands[i + 3] if par3 else commands[commands[i + 3]]

                if p1:
                    i = p2
                else:
                    i += 3
            elif opcode == 6:
                p1 = self.get_mode_value(i + 1, par1)
                p2 = self.get_mode_value(i + 2, par2)
                # p3 = commands[i + 3] if par3 else commands[commands[i + 3]]

                if not p1:
                    i = p2
                else:
                    i += 3
            elif opcode == 7:
                p1 = self.get_mode_value(i + 1, par1)
                p2 = self.get_mode_value(i + 2, par2)
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
                p1 = self.get_mode_value(i + 1, par1)
                p2 = self.get_mode_value(i + 2, par2)
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
            elif opcode == 9:
                p1 = self.get_mode_value(i + 1, par1)
                self.relative_base += p1
                i += 2
            elif opcode == 99:
                yield -1000000
            else:
                print('ERROR!!!')

        return -1000000

with open('input.txt') as fp:
    for line in fp:
        input = line.split(',')
        all_commands = [int(a) for a in input]

# # settings = [4,3,2,1,0]
# options = [0, 1, 2, 3, 4]
#
#
# all_commands = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
all_commands = [1102,34915192,34915192,7,4,7,99,0]

# translate memory to dict
all_commands = {i: val for i, val in enumerate(all_commands)}
amp = Amplifier(all_commands, False)
gen = amp.calculate_output(1, 0)
output = next(gen)
print(output)

while(True):
    output = gen.send(output)
    print(output)
    # output = next(gen)
    if output == -1000000:
        break
    # previous_amp_output = output

#
# options = [5, 6, 7, 8, 9]
#
# # all_commands = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
# # 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# # all_commands = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# # -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# # 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
#
# best_res = -1
# res_phase_settings = None
# for settings in itertools.permutations(options, 5):
#     # create generators
#     generators = []
#     output = 0
#     for setting in settings:
#         amp = Amplifier(all_commands)
#         generators.append(amp.calculate_output(setting, output))
#         output = next(generators[-1])
#     previous_amp_output = output
#     while(True):
#         for gen in generators:
#             output = gen.send(output)
#             # output = next(gen)
#             if output == -1:
#                 break
#         if output == -1:
#             break
#         previous_amp_output = output
#
#     if best_res < previous_amp_output:
#         res_phase_settings = settings
#         best_res = previous_amp_output
#
# # part 2 - 3321777
# print(res_phase_settings)
# print(best_res)
