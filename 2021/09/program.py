with open('input.txt') as file:
    grid = list(list(map(int,list(i))) for i in file.read().split())
print(grid)

lowestCount = 0
width = len(grid[0])-1
height = len(grid)-1
print(height, width,'width')
basins = {}
# def compareNeighbors(x, y):
#     comp = grid[y][x]
#     # print(comp, y, x)
#     equal = []
#     if x >0:
#         print('comp 1')
#         if grid[y][x-1] < comp:
#             return False
#         if grid[y][x-1] == comp:
#             equal.append(True)
#         else:
#             equal.append(False)

#     if x < width:
#         print('comp 2')
#         if grid[y][x+1] < comp:
#             return False
#         if grid[y][x+1] == comp:
#             equal.append(True)
#         else:
#             equal.append(False)
#     if y > 0:
#         print('comp 3')
#         if grid[y-1][x] < comp:
#             return False
#         if grid[y-1][x] == comp:
#             equal.append(True)
#         else:
#             equal.append(False)
#     if y < height:
#         print('comp 4')
#         if grid[y+1][x] < comp:
#             return False
#         if grid[y+1][x] == comp:
#             equal.append(True)
#         else:
#             equal.append(False)
#     print(comp,'I made it',x,y)
#     # if x ==99 or y==99:
#     #     input()
#     if all(i for i in equal):
#         return False
#     return comp +1
# for i in range(width+1):
#     for j in range(height+1):
#         lowestCount += compareNeighbors(i,j)
nums = list(range(10, 1000))
def reset(new,old):
    # print('RESETTING')
    for i in grid:
        for j in range(len(i)):
            if i[j] == old:
                i[j]=new

for i in range(width +1):
    for j in range(height+1):
        if grid[j][i] == 9:
            continue
        newnum = 0
        if i > 0:
            comp = grid[j][i-1]
            if  comp > 9:
                newnum = comp
            if j > 0:
                upcomp = grid[j-1][i]
                if upcomp > 9:
                    if newnum > 9:
                        reset(comp, upcomp)
                    else:
                        newnum = upcomp

        elif j > 0:
            upcomp = grid[j-1][i]
            if upcomp > 9:
                newnum = upcomp
        
        if newnum ==0:
            newnum = nums.pop(0)
        grid[j][i] = newnum
        

# print(nums)

from collections import Counter
flat_list = [item for sublist in grid for item in sublist]
print(Counter(flat_list))
# print(grid)
# print(lowestCount)