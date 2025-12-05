import sys
FILE_NAME = sys.argv[1]

def get_input(file_name: str):
    file = open(file_name)
    ranges_list, ids_list  = [], []

    line = file.readline().strip()
    while line != "":
        ranges_list.append(line)
        line = file.readline().strip()
    
    for line in file:
        ids_list.append(line.strip())
    return ranges_list, ids_list

def part1(ranges: list, ids: list) -> int:
    fresh_count = []
    for rng in ranges:
        num1, num2 = rng.split('-')
        for id in ids:
            if id in fresh_count:
                continue

            if int(num1) <= int(id) <= int(num2):
                fresh_count.append(id)

    return len(fresh_count)


def parse_ranges(ranges: list[str]) -> list[list[int]]:
    rng_tuples = []
    for rng in ranges:
        num1, num2 = rng.split('-')
        rng_tuples += [[int(num1), int(num2)]]
    return rng_tuples

def combine_overlaps(ranges):
    result = []
    rng_tuples = parse_ranges(ranges)
    rng_tuples.sort()
    result.append(rng_tuples[0])

    for curr_rng in rng_tuples[1:]:
        last_merged_interval = result[-1]
        if curr_rng[0] <= last_merged_interval[1]:
            last_merged_interval[1] = max(curr_rng[1], last_merged_interval[1])
        else:
            result.append(curr_rng)

    return result

def part2(ranges: list) -> int:
    ranges = combine_overlaps(ranges)
    fresh_count = 0
    for [one, two] in ranges:
        possible_count = two + 1 - one
        fresh_count += possible_count
    return fresh_count


ranges_list, ids_list = get_input(FILE_NAME)
part1 = part1(ranges_list, ids_list)
print("Part 1:", part1)

part2 = part2(ranges_list)
print("Part 2:", part2)
