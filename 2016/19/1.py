import math

def solve3():
    number = 3014603
    print (number - math.pow(2, math.floor(math.log(number, 2)))) * 2 + 1

def solve4():
    number = 3014603
    elves = range(number)
    winner = 2
    for i in range(4, number+1):
        # index of erased:
        if winner < i/2 - 1:
            winner = winner+1
        else:
            winner = winner+2
        if winner == i:
            winner = 0
    print winner + 1



# solve2()
solve3()
solve4()
# 1113487 too low
# 1420280
