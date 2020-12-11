from copy import deepcopy

grid = []
with open('input.in') as file:
    for line in file.readlines():
        grid.append(list('.'+line.strip()+'.'))
width = len(grid[0])
grid.append(['.']*width)
grid.insert(0,['.']*width)
height = len(grid)

def update(grid):
    grid_copy = deepcopy(grid)
    for y in range(1,height-1):
        for x in range(1,width-1):
            if grid[y][x] == '.':
                continue
            elif grid[y][x] == 'L':
                adjacent_seats = ''
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        adjacent_seats += grid[y+j][x+i]
                if not '#' in adjacent_seats:
                    grid_copy[y][x] = '#'
            elif grid[y][x] == '#':
                adjacent_seats = ''
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        adjacent_seats += grid[y+j][x+i]
                if adjacent_seats.count('#')>=5:
                    grid_copy[y][x] = 'L'

            else:
                raise Exception
    return grid, grid_copy

prev_grid, grid = update(grid)
while prev_grid != grid:
    prev_grid, grid = update(grid)

print(sum(g.count('#') for g in grid))
# for i in grid:
#     print(i)