
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

    print(sum)

part1()