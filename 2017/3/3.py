input = []
with open('input') as fp:
    for line in fp:
        num = int(line)
#   print num
    is_smaller = True
    index = 1
    circle_dis = 0
    while num - 1 >= index * index:
        index += 2
        circle_dis += 1

    circle_side_dist = abs(((((num - 1 - ((index - 2) * (index - 2))) + 1) % (8 * circle_dis)) % (circle_dis * 2)) - circle_dis)

    print circle_dis + circle_side_dist

side_dis = 100
array = [[0 for i in range(side_dis)] for j in range(side_dis)]

# 2nd TASK
def print_array(arra):
    for arr in arra:
        print(' '.join(map(str, arr)))


def insert(x, y, val):
    array[x + side_dis/2][y + side_dis/2] = val


def get(x, y):
    return array[x + side_dis / 2][y + side_dis / 2]

insert(0, 0, 1)


loc = [0, 0]
limit = 0
change = [1, 0]
i = 0
while i < 1000000:
    if loc[0] == limit and loc[1] == -limit:
        limit += 1
        change = [1, 0]
    elif loc[0] == limit and loc[1] == -limit + 1:
        change = [0, 1]
    elif loc[0] == limit and loc[1] == limit:
        change = [-1, 0]
    elif loc[0] == -limit and loc[1] == limit:
        change = [0, -1]
    elif loc[0] == -limit and loc[1] == -limit:
        change = [1, 0]

    val = (get(loc[0]-1, loc[1]-1) +
           get(loc[0]-1, loc[1]) +
           get(loc[0]-1, loc[1]+1) +
           get(loc[0], loc[1]-1) +
           get(loc[0], loc[1]) +
           get(loc[0], loc[1]+1) +
           get(loc[0]+1, loc[1]-1) +
           get(loc[0]+1, loc[1]) +
           get(loc[0]+1, loc[1]+1))
    if val > num:
        print val
        break
    insert(loc[0], loc[1], val)
    loc[0] += change[0]
    loc[1] += change[1]
    i += 1

#print_array(array)
#print get(1,1)