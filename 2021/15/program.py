with open('input.txt') as file:
    matrix = [list(map(int,line)) for line in file.read().split()]

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from copy import deepcopy
def printt(g):
    for l in g:
        print(l)

#remove this or it won't work
# matrix = [[1,20,1,1,1],[1,20,1,20,1],[1,1,1,20,1]]
newMatrix = deepcopy(matrix)
def add1(matrix):
    grid = deepcopy(matrix)
    for line in range(len(grid)):
        for digit in range(len(grid[0])):
            grid[line][digit] += 1
            if grid[line][digit] >= 10:
                grid[line][digit] =1
    return grid
def addMatrix(matrix1, matrix2):
    return deepcopy(matrix1) + deepcopy(matrix2)
def appendMatrix(matrix1,matrix2):
    newMatrix=[]
    for i in range(len(matrix1)):
        newMatrix.append(deepcopy(matrix1[i])+deepcopy(matrix2[i]))
    return newMatrix
# print(add1(matrix))
# print(matrix)
matrix2 = add1(matrix)
matrix3 = add1(add1(matrix))
matrix4 = add1(add1(add1(matrix)))
matrix5 = add1(add1(add1(add1(matrix))))
matrix6 = add1(add1(add1(add1(add1(matrix)))))
matrix7 = add1(add1(add1(add1(add1(add1(matrix))))))
matrix8 = add1(add1(add1(add1(add1(add1(add1(matrix)))))))
matrix9 = add1(add1(add1(add1(add1(add1(add1(add1(matrix))))))))
newMatrix1 = addMatrix(addMatrix(addMatrix(addMatrix(matrix,matrix2),matrix3),matrix4),matrix5)
newMatrix2 = addMatrix(addMatrix(addMatrix(addMatrix(matrix2,matrix3),matrix4),matrix5),matrix6)
newMatrix3 = addMatrix(addMatrix(addMatrix(addMatrix(matrix3,matrix4),matrix5),matrix6),matrix7)
newMatrix4 = addMatrix(addMatrix(addMatrix(addMatrix(matrix4,matrix5),matrix6),matrix7),matrix8)
newMatrix5 = addMatrix(addMatrix(addMatrix(addMatrix(matrix5,matrix6),matrix7),matrix8),matrix9)
totalMatrix = appendMatrix(appendMatrix(appendMatrix(appendMatrix(newMatrix1, newMatrix2), newMatrix3),newMatrix4),newMatrix5)
# print(totalMatrix)
# exit()
width = len(totalMatrix[0])
height = len(totalMatrix)
grid = Grid(matrix = totalMatrix)

start = grid.node(0,0)
end = grid.node(width-1, height-1)
finder = AStarFinder()
path, runs = finder.find_path(start, end, grid)
print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))
print(path)
summ = - totalMatrix[0][0]
for p in path:
    summ += totalMatrix[p[1]][p[0]]
print(summ)
# pathGrid = []
# for _ in range(height):
#     pathGrid.append([0]*width)
# printt(pathGrid)
