from collections import Counter

with open('input.txt') as fp:
    for line in fp:
        numbers = [int(a) for a in line.split()[0]]

width = 25
height = 6
best_layer_0 = 10000000
best_layer_res = -1
message = [2] * width * height

layers = []
for i, number in enumerate(numbers):
    layer_part = []
    if i % (width * height) == 0:
        layer = numbers[i:i + (width * height)]
        count = Counter(layer)
        if count[0] < best_layer_0:
            best_layer_0 = count[0]
            best_layer_res = count[1] * count[2]

        for j, el in enumerate(layer):
            if (layer[j] == 0 or layer[j] == 1) and message[j] == 2:
                message[j] = layer[j]

res = ''
message = ['o' if let == 1 else ' ' for let in message]
# message = list(map(str, message))
# part 1 1792
for numbers_i in range(0, len(message), width):

    print(''.join(message[numbers_i:numbers_i + width]))
print(best_layer_res)
