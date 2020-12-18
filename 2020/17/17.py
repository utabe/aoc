import numpy as np

num_generations = 6

starting_grid = np.asarray([list(i) for i in open('input.in').read().split('\n')])

width,length = starting_grid.shape


# Trying to take advantage of the symmetries across the z=0 and w=0 hyperplanes
grid = np.full((num_generations+1,num_generations+1,width + 2*num_generations,length + 2*num_generations), '.')

idx = tuple([0,0, slice(len(grid[0][0])//2 - width//2,len(grid[0][0])//2 + width//2 + (width%2)), slice(len(grid[0][0])//2 - length//2,len(grid[0][0])//2 + length//2 +(length%2))])

grid[idx] = starting_grid


# if on the w=0 hyperplane we need to double count the w=1, same for z=0. If on the w=0 AND z=0 plane, need to quadruple count. 
def get_num_alive_neighbors(grid, index):
    idx = tuple(slice(max(0,point - 1), point + 2) for point in np.r_[index])
    neighbors = np.count_nonzero(grid[idx]=='#')

    if index[0]==0:
        neighbors = 2*neighbors - np.count_nonzero(grid[(0,idx[1],idx[2],idx[3])]=='#')
    if index[1]==0:
        neighbors = 2*neighbors - np.count_nonzero(grid[(idx[0],0,idx[2],idx[3])]=='#')
    if index[0]==0 and index[1]==0:
        neighbors -= np.count_nonzero(grid[(1,0,idx[2],idx[3])]=='#')
    return neighbors


for i in range(num_generations):
    grid_copy = grid.copy()
    it = np.nditer(grid, flags=['multi_index'])
    while not it.finished:
        idx = it.multi_index
        if it[0] == '.':
            if get_num_alive_neighbors(grid=grid, index=idx) == 3:

                grid_copy[idx] = '#'

        elif it[0] == '#':

            num_neighbors = get_num_alive_neighbors(grid=grid, index=idx)

            if not ((num_neighbors == 3) or (num_neighbors == 4)):
                grid_copy[idx] = '.'
 
        else:
            raise ValueError(f'Unexpected value {it[0]} at {idx}')

        is_not_finished = it.iternext()

    grid = grid_copy


# Similar to the above. The z=0 and w=0 plane needs only be counted once, the z=0 and the w=0 hyperplanes counted twice, and evertything else four times.

double = np.count_nonzero(grid=='#')*2 -np.count_nonzero(grid[0]=='#')
quad = double*2 - 2*np.count_nonzero(grid[0]=='#')
final = quad + np.count_nonzero(grid[0][0]=='#')
print(final)
    
