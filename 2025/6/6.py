import sys

file_name = sys.argv[1]
file = open(file_name)

math = []

for line in file:
    objects = line.strip().split()
    math.append(objects)

rows_sz = len(math)
cols_sz = len(math[0])

def do_op(op, nums):
    result = int(nums[0])
    if op == '+':
        for num in nums[1:]:
            result+=int(num)
    elif op == "*":
        for num in nums[1:]:
            result*=int(num)
    return result

def part1(math):
    sum_of_ops = 0
    for i in range(len(math[0])):
        operation = math[-1][i]
        nums = []
        for j in range((len(math)-1)):
            nums.append(math[j][i])
        
        result = do_op(operation, nums)
        sum_of_ops += result
    return sum_of_ops

print(f"Part 1: {part1(math)}")