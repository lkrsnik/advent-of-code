from collections import Counter

input = []
with open('input') as fp:
    for line in fp:
        input.append(line.split()[0])

twos=0
threes=0

for el in input:
    counts = Counter(el)
    if 2 in counts.values():
        twos += 1

    if 3 in counts.values():
        threes += 1


print(twos * threes)


def diff_letters(a,b):
    return sum(a[i] != b[i] for i in range(len(a)))

cor_i = ""
cor_j = ""
for i in input:
    for j in input:
        if diff_letters(i, j) == 1:
            cor_i = i
            cor_j = j

r = ""
for i in range(len(cor_i)):
    if cor_i[i] == cor_j[i]:
        r += cor_i[i]

print(r)
