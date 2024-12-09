import re
import functools

def read(path: str) -> str:
    with open(path) as fp:
        text = fp.read()
    return text

text = read('input.txt')
# part 1
multiplications = re.findall('mul\(\d+,\d+\)', text)
cumulative = 0
for multiplication in multiplications:
    cumulative += functools.reduce(lambda a,b: a*b, [int(num) for num in re.findall('\d+', multiplication)])
print(cumulative)

# part 2
multiplications = re.findall('(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', text)
cumulative = 0
additions_enabled = True
for multiplication in multiplications:
    if multiplication == 'don\'t()':
        additions_enabled = False
        continue
    if multiplication == 'do()':
        additions_enabled = True
        continue
    if additions_enabled: 
        cumulative += functools.reduce(lambda a,b: a*b, [int(num) for num in re.findall('\d+', multiplication)])
print(cumulative)