import sys

file_name = sys.argv[1]
file = open(file_name)

def parse1(name):
    file = open(name)
    math = []

    for line in file:
        objects = line.strip().split()
        math.append(objects)
    file.close()
    return math

def do_op(op, nums):
    if not nums:
        return 0
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
    for i in range(len(math[0])): # go through each number in row 0
        operation = math[-1][i]
        nums = []
        for j in range((len(math)-1)): # get each number in column
            nums.append(math[j][i])
        
        result = do_op(operation, nums)
        sum_of_ops += result
    return sum_of_ops


def parse2(name):
    math = []
    file = open(name)

    for line in file:
        math.append(line.rstrip('\n'))

    file.close()
    return math


def part2(math):
    sum_of_ops = 0
    width = len(math[0])        # total character width
    height = len(math) - 1      # last row = operators
    ops = math[-1].split()
    

    for op in ops:
        all_nums_by_column = []


    
    new_nums = []
    for col in range(width):
        #operation = ops[col]
        nums_in_col = []
        max_len = 0

        # extract vertical numbers by character column
        for row in range(height):
            ch = math[row][col]
            if ch.isdigit():
                nums_in_col.append(ch)
                max_len = max(max_len, len(ch))
        
        if nums_in_col:
            new_nums.append(''.join(nums_in_col))

    op_positions = [] # do problems by getting how many numbs are in each operation
    for i, ch in enumerate(math[-1]):
        if ch == '+' or ch == '*':
            op_positions.append(i)

    for i, value in enumerate(op_positions):
        if i == len(op_positions) - 1:
            print("len of ops", (len(math[-1])-1), op_positions[i])
            op_positions[i] = ((len(math[-1])-1) - op_positions[i]) + 1
            continue

        op_positions[i] = op_positions[i+1] - (op_positions[i] + 1)
    
    start = 0 # final calc
    for idx, op in enumerate(ops):
        nums_in_problem = op_positions[idx]
        sum_of_ops += do_op(op,new_nums[start: start+nums_in_problem] )
        start += nums_in_problem
    return sum_of_ops

print(f"Part 1: {part1(parse1(file_name))}")
print(f"Part 2: {part2(parse2(file_name))}")

