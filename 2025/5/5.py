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
                print(f"id is in a range {id}")
                #current_ids.remove(id)
                fresh_count.append(id)

    return len(fresh_count)

ranges_list, ids_list = get_input(FILE_NAME)
#print(ids_list)

part1 = part1(ranges_list, ids_list)
print("Part 1:", part1)
