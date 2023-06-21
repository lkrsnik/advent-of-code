input = []
with open('input') as fp:
    for line in fp:
        input.append(line.replace(',', '').split())

connections = []
for el in input:
    connections.append(map(int, el[2:]))


i = 0
# for prog in connections:
#     for con in prog:
#         if i not in connections[con]:
#             connections[con].append(i)
#     i += 1

group = []
def recursion(id):
    if id in group:
        return
    group.append(id)
    for el in connections[id]:
        recursion(el)

recursion(0)

print len(group)





group = []
tot_groups = 0
for i in range(len(connections)):
    if i not in group:
        recursion(i)
        tot_groups += 1


print tot_groups
