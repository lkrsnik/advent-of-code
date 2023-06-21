from collections import Counter

rang = [206938, 679128]


def find_dup_char(input):
    for i in Counter(input).values():
        # part 1
        # if (i > 1):
        #     return True
        # part 2
        if (i == 2):
            return True

    return False


res = 0
i = 206938
while i < 679128:
    stri = str(i)
    if ''.join(sorted(stri)) == stri and find_dup_char(stri):
        res += 1
    i += 1

print(res)
