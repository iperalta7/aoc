import sys

with open(sys.argv[1], "r") as f:
    ranges_list = f.readline().strip().split(',')

def is_valid_id(id: str):
    if len(id) % 2 == 1:
        return True
    length = len(id)
    lead = id[:(length//2)]
    end =  id[(length//2):]
    #print(f"lead {lead}, end {end}")
    if lead == end:
        return False

    return True

def part1():
    invalids_sum = 0
    numbers = []
    for rnge in ranges_list:
        num1, num2 = rnge.split("-")
        numbers += [num for num in range(int(num1),int(num2))]

    for num in numbers:
        if is_valid_id(str(num)):
            continue

        print(f"P1: Invalid id: {num}")
        invalids_sum += num

    print(f"P1: Sum of invalid ids: {invalids_sum}")

def is_valid_id_2(id: str):
    if not is_valid_id(id):
        return False
    
    multiples = [] # 1, 2
    for num in range(1, len(id)): # get factors of the length to go through each possible rep
        if len(id) % num == 0:
            multiples += [num]
    
    check = "" 
    for number in multiples: # create each possible rep and check against id
        temp = id[:number]
        check = ""
        for _ in range(len(id)//number):
            check += temp

        print(f" factors {multiples} check {check} id {id}")
        if check == id:
            return False

    if check == id:
        return False
    
    return True

def part2():
    invalids_sum = 0
    numbers = []
    for rnge in ranges_list:
        num1, num2 = rnge.split("-")
        numbers += [num for num in range(int(num1),int(num2))]

    for num in numbers:
        if is_valid_id_2(str(num)):
            continue

        print(f"P2: Invalid id: {num}")
        invalids_sum += num

    print(f"P2: Sum of invalid ids: {invalids_sum}")

part1()
part2()