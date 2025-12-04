import sys

grid = []
file_name = sys.argv[1]
file = open(file_name)
for line in file:
    grid.append(line.strip())

row_size = len(grid)
col_size = len(grid[0])

def in_bound(i, j):
    if i < 0 or j < 0:
        return False
    if i > row_size-1 or j > col_size-1:
        return False
    

def count_neighbors(i, j):
    count = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if (x,y) == (i,j):
                continue

            if x < 0 or x > row_size - 1:
                continue

            if y < 0 or y > col_size - 1:
                continue

            #print((x,y))
            if grid[x][y] == "@":
                count+=1
    return count

def part1():
    count = 0
    for i in range(row_size):
        for j in range(col_size):
            if grid[i][j] != "@":
                continue
            
            if count_neighbors(i, j) < 4:
                count+=1
    return count

def part2():
    total = 0
    new_grid = grid
    while True:
        count = 0
        indices_to_remove = []
        for i in range(row_size):
            for j in range(col_size):
                if new_grid[i][j] != "@":
                    continue
                
                if count_neighbors(i, j) < 4:
                    indices_to_remove.append((i,j))
                    count+=1

        if count == 0:
            break

        for (i,j) in indices_to_remove:
            line = list(new_grid[i])
            line[j] = "x"
            new_grid[i] = ''.join(line)
        
        total += count
    return total


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")