import re
import functools

def read(path: str) -> str:
    with open(path, 'r') as fp:
        text = fp.read()
    return text

# input_path = 'input-example.txt'
input_path = 'input.txt'

text = read(input_path)
rules_raw, samples = text.split('\n\n')
rules_list = [tuple(list(map(int, rule.split('|')))) for rule in rules_raw.split('\n')]
rules = {}
# populate rules
for rule in rules_list:
    if rule[0] not in rules:
        rules[rule[0]] = []
    rules[rule[0]].append(rule[1])
samples = [list(map(int, sample.split(','))) for sample in samples.strip().split('\n')]

# part 1
def check_rules(num: int, check_list: list[int]) -> int:
    if num not in rules:
        return True
    return all(list(map(lambda x: x not in rules[num], check_list)))

middle_sum = 0
for sample in samples:
    if all([check_rules(sample[pos], sample[:pos]) for pos in range(len(sample))]):
        middle_sum += sample[len(sample)//2]

# part 2
def identify_mistakes(num: int, possible_mistakes: list[int]) -> int|None:
    for i, possible_mistake in enumerate(possible_mistakes):
        if num not in rules:
            continue
        if possible_mistake in rules[num]:
            return i
    return None

def swap(p1, p2, sample):
    v1 = sample[p1]
    v2 = sample[p2]
    sample[p1] = v2
    sample[p2] = v1

middle_sum = 0
for sample_i in range(len(samples)):
    sample = samples[sample_i]
    has_mistake = False
    for pos in range(len(sample)):
        mistake = identify_mistakes(sample[pos], sample[:pos])
        while mistake is not None:
            has_mistake = True
            swap(pos, mistake, sample)
            mistake = identify_mistakes(sample[pos], sample[:pos])

    if has_mistake:
        middle_sum += sample[len(sample)//2]

print(middle_sum)
