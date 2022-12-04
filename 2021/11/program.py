with open('input.txt') as file:
    grid = [list(map(int,list(s))) for s in file.read().split()]
import copy
# for g in grid:
#     g = list(map(int,g))
print(grid)
def printt(key):
    for l in key:
        print(l)
def addNeighbors(idx, i, grid):
    # print('called on ',idx,i)
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if idx+y < 0 or idx + y >9 or i +x < 0 or i+x > 9 or grid[idx +y][i+x]==-1: 
                continue
            grid[idx+y][i+x] +=1
    grid[idx][i] = -1
    return grid

def step(grid, cnt):
    #add 1 to everything
    for idx in range(len(grid)):
        grid[idx] = [i+1 for i in grid[idx]]
    #glow the neigbors
    while any(x >= 10 for line in grid for x in line):
        for idx in range(len(grid)):
            for i in range(len(grid[idx])):
                if grid[idx][i] >= 10:
                    grid = copy.deepcopy(addNeighbors(idx, i, grid))
    # printt(grid)
    # input()
    #reset to zero
    for idx in range(len(grid)):
        for i in range(len(grid[idx])):
            if grid[idx][i] == -1:
                grid[idx][i]=0
                cnt +=1
    return grid, cnt
        # for i in line:
        #     i = i +1
cnt = 0
for _ in range(1000):
    grid, cnt = copy.deepcopy(step(grid, cnt))
    if all(x ==0 for line in grid for x in line):
        print(_ +1, 'synchronize here')
        break
printt(grid)
print('count',cnt)