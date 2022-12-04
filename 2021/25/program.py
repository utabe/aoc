with open('input.txt') as file:
    grid = [list(x) for x in file.read().split()]

def printt(d):
    for x in d:
        print(x)
    
printt(grid)
from copy import deepcopy as dc
def move(grid):
    newGrid = dc(grid)
    anyMoved = False

    #move right
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '>':
                if x == len(grid[0]) -1:
                    if grid[y][0] == '.':
                        newGrid[y][0] = '>'
                        newGrid[y][x] = '.'
                        anyMoved = True
                elif grid[y][x+1] =='.':
                    newGrid[y][x+1] = '>'
                    newGrid[y][x] = '.'
                    anyMoved = True
    grid = dc(newGrid)

    #move down
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'v':
                if y == len(grid) -1:
                    if grid[0][x] == '.':
                        newGrid[0][x] = 'v'
                        newGrid[y][x] = '.'
                        anyMoved = True
                elif grid[y+1][x] =='.':
                    newGrid[y+1][x] = 'v'
                    newGrid[y][x] = '.'
                    anyMoved = True
    return dc(newGrid), anyMoved
counter = 0
anyMoved = True
while anyMoved:
    grid, anyMoved = move(grid)
    counter +=1

# for _ in range(58):
print('=================')
# printt(grid)
print(counter)