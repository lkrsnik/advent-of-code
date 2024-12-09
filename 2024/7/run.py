import copy
from itertools import product


def read(path: str) -> str:
    with open(path, 'r') as fp:
        text = fp.read()
    return text

# input_path = 'input-example.txt'
input_path = 'input.txt'

text = read(input_path).strip()

# calculations = [(int(row.split(': ')[0]), [num for num in row.split(': ')[1].split(' ')]) for row in text.split('\n')]

# part 0 with precedence rule :(
# def test_combinations(numbers, result):
#     signs = ['+', '*']
#     arg = [signs] * (len(numbers) - 1)
#     cart_product = list(product(*arg))
#     for signs in cart_product:
#         calc = numbers[0]
#         for sign, num in zip(signs, numbers[1:]):
#             calc += sign + num
#         if eval(calc) == result:
#             return True
#
#     return False
#
# summar = 0
# for calculation in calculations[-1:]:
#     if test_combinations(calculation[1], calculation[0]):
#         summar += calculation[0]

# part 1
calculations = [(int(row.split(': ')[0]), [int(num) for num in row.split(': ')[1].split(' ')]) for row in text.split('\n')]


def add_rec(inter_results, other_nums):
    current_calculations = []
    if not other_nums:
        return inter_results
    for r in inter_results:
        current_calculations.append(r * other_nums[0])
        current_calculations.append(r + other_nums[0])
        # DELETE THIS LINE FOR P1
        current_calculations.append(eval(f'{r}{other_nums[0]}'))
    return add_rec(current_calculations, other_nums[1:])


def test_combinations(numbers, result):
    possible_results = add_rec([numbers[0]], numbers[1:])
    return result in possible_results

summar = 0
for calculation in calculations:
    if test_combinations(calculation[1], calculation[0]):
        summar += calculation[0]

print(summar)