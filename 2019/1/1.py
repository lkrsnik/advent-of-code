input = []
with open('input.txt') as fp:
    for line in fp:
        input.append(int(line.split()[0]))

# part 1
res1 = sum(map(lambda a: int(a/3) - 2, input))

# part 2
res2 = sum(map((lambda a: lambda v: a(a, v))(lambda s, x: s(s, int(x / 3) - 2) + int(x / 3) - 2 if int(x/3) - 2 > 0 else 0), input))

# 3443395
print(res1)
# 5162216
print(res2)
