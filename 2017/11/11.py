from collections import Counter
import copy

input = []
with open('input') as fp:
    for line in fp:
        input = line.split(',')

# occ = dict(Counter(input))
# if 'n' not in occ:
#     occ['n'] = 0
# if 'ne' not in occ:
#     occ['ne'] = 0
# if 'se' not in occ:
#     occ['se'] = 0
# if 's' not in occ:
#     occ['s'] = 0
# if 'sw' not in occ:
#     occ['sw'] = 0
# if 'nw' not in occ:
#     occ['nw'] = 0
# old_occ = copy.copy(occ)
# occ['sw'] = old_occ['sw'] - old_occ['ne'] if old_occ['ne'] < old_occ['sw'] else 0
# occ['se'] = old_occ['se'] - old_occ['nw'] if old_occ['nw'] < old_occ['se'] else 0
#
#
# occ['nw'] = old_occ['nw'] - old_occ['se'] if old_occ['se'] < old_occ['nw'] else 0
# occ['ne'] = old_occ['ne'] - old_occ['sw'] if old_occ['sw'] < old_occ['ne'] else 0
#
# north = min(occ['nw'], occ['ne'])
# occ['n'] += north
# occ['nw'] -= north
# occ['ne'] -= north
#
# south = min(occ['sw'], occ['se'])
# occ['s'] += south
# occ['sw'] -= south
# occ['se'] -= south
#
# old_occ = copy.copy(occ)
# occ['s'] = old_occ['s'] - old_occ['n'] if old_occ['n'] < old_occ['s'] else 0
# occ['n'] = old_occ['n'] - old_occ['s'] if old_occ['s'] < old_occ['n'] else 0
#
#
#
# print occ
#
# res = 0
# if occ['s']:
#     if occ['se'] or occ['sw']:
#         res = occ['s'] + occ['se'] + occ['sw']
#     else:
#         res = max(occ['s'], occ['ne'], occ['nw'])
# else:
#     if occ['ne'] or occ['nw']:
#         res = occ['n'] + occ['ne'] + occ['nw']
#     else:
#         res = max(occ['n'], occ['se'], occ['sw'])
#
# print res
dist = 0
se = 0
sw = 0
s = 0
max_dist = -1000
for el in input:
    if el == 'se':
        se += 1
    elif el == 'sw':
        sw += 1
    elif el == 's':
        s += 1
    elif el == 'nw':
        se -= 1
    elif el == 'ne':
        sw -= 1
    else:
        s -= 1

    if s >= 0 and se >= 0 and sw >= 0:
        dist = s + max(se, sw)
    elif s <= 0 and se <= 0 and sw <= 0:
        dist = abs(s + min(se, sw))
    elif s >= 0 and se >= 0 and sw <= 0:
        dist = max(s, abs(sw)) + se
    elif s >= 0 and se <= 0 and sw >= 0:
        dist = max(s, abs(se)) + sw
    elif s >= 0 and se <= 0 and sw <= 0:
        dist = abs(s - abs(min(se, sw)))
    elif s <= 0 and se >= 0 and sw >= 0:
        dist = abs(abs(s) - max(se, sw))
    elif s <= 0 and se >= 0 and sw <= 0:
        dist = max(abs(s), se) + abs(sw)
    elif s <= 0 and se <= 0 and sw >= 0:
        dist = max(abs(s), sw) + abs(se)

    if max_dist < dist:
        max_dist = dist

print dist
print max_dist