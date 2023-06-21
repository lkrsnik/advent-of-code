import copy
input = []


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
            extended_circle[current_position:current_position+length] = extended_circle[current_position:current_position+length][::-1]
            circle = extended_circle[circle_length:current_position+circle_length]
            circle.extend(extended_circle[current_position:circle_length])
            current_position = (current_position + length + skip_size) % circle_length
            skip_size += 1

    return circle


def getHash(input):
    input.extend([17, 31, 73, 47, 23])

    sequence = rotate(input, rounds=64)

    res = ''
    res2 = []
    for i in range(0, 256, 16):
        xor = 0
        for el in sequence[i:i + 16]:
            xor ^= el
        res += hex(xor)[2:].zfill(2)

    return res

with open('input') as fp:
    for line in fp:
        input = [ord(c) for c in line]


def to_binary(hex):
    scale = 16  ## equals to hexadecimal
    num_of_bits = 8
    res = ''
    for i in range(0, len(hex), 2):
        my_hexdata = hex[i:i+2]
        res += str(bin(int(my_hexdata, scale))[2:].zfill(num_of_bits))
    return res

size = 128
input.append(ord('-'))
hashes = []
ones_sum = 0
for i in range(size):
    base = copy.copy(input)
    base.extend([ord(c) for c in str(i)])
    # print base
    h = getHash(base)
    bin_hash = to_binary(h)
    ones_sum += bin_hash.count('1')
    hashes.append(list(bin_hash))

# too low 8108
print ones_sum


# part 2
def checker(x, y):
    checked[x][y] = True
    if hashes[x][y] == '1':
        if x+1 < size and not checked[x+1][y]:
            if hashes[x+1][y] == '1':
                checker(x+1, y)
        if x-1 >= 0 and not checked[x-1][y]:
            if hashes[x-1][y] == '1':
                checker(x-1, y)
        if y+1 < size and not checked[x][y+1]:
            if hashes[x][y+1] == '1':
                checker(x, y+1)
        if y-1 >= 0 and not checked[x][y-1]:
            if hashes[x][y-1] == '1':
                checker(x, y-1)
        return 1
    else:
        return 0

checked = [[False for i in range(size)] for i in range(size)]

num_groups = 0
for i in range(size):
    for j in range(size):
        if not checked[i][j]:
            num_groups += checker(i,j)

print num_groups
