
import sys

file_name = sys.argv[1]
file = open(file_name)

banks = [list(map(int, line.strip())) for line in file]

def find_biggest_num(bank):
    # last digit can never be the first
    # next digit form first must come after
    left = max(bank[:-1])
    left_index = bank.index(left)
    right = max(bank[left_index+1:])
    return int(f"{left}{right}")

def part1():
    sum = 0
    for bank in banks:
        sum += find_biggest_num(bank)
    return sum

# this code can be cleaned up
def big_num_window(bank):
    nums = []
    current_window_size = 12
    window = bank[:len(bank) - 11]

    prev_left_idx = 0
    for i in range(12):
        next_max_num = max(window)
        nums.append(next_max_num)

        # enforce correct new left shift
        new_left_idx = window.index(next_max_num) + prev_left_idx + 1

        #  enforce remaining window size
        remaining = 12 - len(nums) + 1
        new_right_idx = len(bank) - remaining + 1

        window = bank[new_left_idx:new_right_idx]
        prev_left_idx = new_left_idx

    return int(''.join(map(str, nums)))

def part2():
    sum = 0
    for bank in banks: # 
        num = big_num_window(bank)
        sum += num
    return sum

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")