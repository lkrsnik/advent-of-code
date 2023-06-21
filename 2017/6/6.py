import copy

with open('input') as fp:
    for line in fp:
        input = map(int, line.split())

print input

current_state = input
states = []
loop_num = 0
while current_state not in states:
    loop_num += 1
    states.append(copy.copy(current_state))
    max_value = max(current_state)
    index = current_state.index(max_value)
    current_state[index] = 0
    for i in range(max_value):
        index = (index + 1) % len(current_state)
        current_state[index] += 1
print loop_num
print len(states) - states.index(current_state)