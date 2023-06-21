input = ''
with open('input') as fp:
    for line in fp:
        input = line

#print input
# erase !
temp = ''
erase = False
for let in list(input):
    if erase:
        erase = False
        continue
    if let == '!':
        erase = True
        continue
    temp += let
#print temp

# erase <>
temp2 = ''
erase = False
garbage_num = 0
for let in list(temp):
    if let == '<':
        erase = True
    elif let == '>':
        erase = False
        garbage_num -= 1
        continue
    if erase:
        garbage_num += 1
        continue
    temp2 += let

#print temp2

string = temp2.replace('{', '[').replace('}', ']')
string2 = ''
i = 0
for let in string:
    if let == ',':
        if list(string)[i-1] != ']' or list(string)[i+1] != '[':
            i += 1
            continue
    string2 += let
    i += 1
#print string
#print string2
arr = eval(string2)
#print arr

def recursion(arr, val):
    val_sum = val
    for el in arr:
        val_sum += recursion(el, val + 1)

    return val_sum

print recursion(arr, 1)

print garbage_num
