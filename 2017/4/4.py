from collections import Counter

input = []
with open('input') as fp:
    for line in fp:
        input.append(line.split())

print(len(input) - sum([1 if sum([0 if el == 1 else 1 for el in Counter(line).values()]) > 0 else 0 for line in input]))

# from itertools import permutations

# valid_pass = 0
# for line in input:
#     perms = []
#     valid = True
#     for word in line:
#         if word in perms:
#             valid = False
#         perms.extend([''.join(p) for p in permutations(word)])
#     if valid:
#         valid_pass += 1
#
# print valid_pass
