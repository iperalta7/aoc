import sys

FILE = open(sys.argv[1], "r")
DIR = {'L': -1, 'R': 1}
START = 50
MAX = 100

def part_1():
    FILE.seek(0)
    position = START
    count = 0
    for line in FILE:
        direction = DIR[line[0]]
        num = int(line[1:])
        new_pos = (position + (direction * num)) % MAX

        if new_pos == 0:
            count += 1

        position = new_pos

    print(count)

def part_2():
    FILE.seek(0)  # reset file pointer
    zero_rotations = 0
    position = START

    for line in FILE:
        dir = DIR[line[0]]
        num = int(line[1:])
        prev = position
        steps = num * dir
        zero_rotations += int(abs(steps) / 100) # Full wraps
        position = (position + steps) % 100
        if prev != 0 and position != 0:
            if (steps < 0 and position > prev) or \
                steps > 0 and position < prev: 
                zero_rotations += 1 # Wrap

        if position == 0:
            zero_rotations += 1

    print(zero_rotations)


part_1()
part_2()
FILE.close()