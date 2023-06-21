class Marble:

    def __init__(self, number, left, right):
        self.number = number
        self.left = left
        self.right = right

    def add(self, number):
        # prev_marble = marble.right
        # next_marble = marble.right.right
        new_marble = Marble(number, marble.right, marble.right.right)
        marble.right.right.left = new_marble
        marble.right.right = new_marble
        return new_marble

    def delete(self):
        del_marble = self.left.left.left.left.left.left.left
        del_marble.left.right = del_marble.right
        del_marble.right.left = del_marble.left
        return del_marble.right, del_marble.number


marble = Marble(0, None, None)
marble.left = marble
marble.right = marble
# marble = marble.add(1)
# marble = marble.add(2)
# marble = marble.add(3)
# marble = marble.add(4)
# n_players = 9
# scores = [0] * n_players
# last_marble = 25
# state = [0]

# n_players = 9
# scores = [0] * n_players
# last_marble = 50
# state = [0]

# n_players = 10
# scores = [0] * n_players
# last_marble = 1618
# state = [0]

# n_players = 30
# scores = [0] * n_players
# last_marble = 5807
# state = [0]

n_players = 430
scores = [0] * n_players
last_marble = 7158800
state = [0]

# i = 0
# p = 0
pl = 0
for m in range(1, last_marble+1):
    if m % 23 != 0:
        marble = marble.add(m)
    else:
        marble, num = marble.delete()
        scores[pl] += m + num
    pl = (pl + 1) % n_players
    # if marble % 1000 == 0:
    #     print(marble)
    #     print(marble/last_marble)





# i = 0
# p = 0
# pl = 0
# for marble in range(1, last_marble+1):
#     if marble % 23 != 0:
#         p = i % len(state) + 1
#         i = p
#         state.insert(p, marble)
#         # +1 because of next element +1 because we add element
#         i = (i + 1) % (len(state) + 1)
#         # i = (i + 1) % len(state)
#     else:
#         i = ((i - 8) + len(state)) % len(state)
#         scores[pl] += marble + state[i]
#         del state[i]
#         i += 1
#     pl = (pl + 1) % n_players
#     # if marble % 1000 == 0:
#     #     print(marble)
#     #     print(marble/last_marble)
#     # print(state)

print(max(scores))
# print(r)
