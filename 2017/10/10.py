import copy
# input = ''
# with open('input') as fp:
#     for line in fp:
#         input = map(int, line.split(','))
#
# # print input
def rotate(input, rounds=1):
    circle_length = 256
    circle = range(circle_length)
    # print circle

    current_position = 0
    skip_size = 0
    for i in range(rounds):
        for length in input:
            extended_circle = copy.copy(circle)
            extended_circle.extend(circle)
            # print extended_circle
            extended_circle[current_position:current_position+length] = extended_circle[current_position:current_position+length][::-1]
            # print extended_circle
            circle = extended_circle[circle_length:current_position+circle_length]
            circle.extend(extended_circle[current_position:circle_length])
            #print circle
            # circle = extended_circle[current_position:current_position+circle_length]
            current_position = (current_position + length + skip_size) % circle_length
            skip_size += 1
        # print circle
        # break

    return circle
#
# print('P1')
# circle = rotate(input)
# print circle[0] * circle[1]

# ----------------------------------------------------------------------------
print('P2')
input = []
with open('input') as fp:
    for line in fp:
        input = [ord(c) for c in line]

input.extend([17, 31, 73, 47, 23])


sequence = rotate(input, rounds=64)

res = ''
res2 = []
for i in range(0, 256, 16):
    xor = 0
    for el in sequence[i:i+16]:
        xor ^= el
    res += hex(xor)[2:].zfill(2)

    res2.append(hex(xor))

# wrong 4db3799145278dc9f73dcdbc68bd53d
print(res)