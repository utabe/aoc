with open('input.txt') as file:
    vents = file.read().split('\n')
width = 1000
grid = [0]*(width*width)

# print(grid, vents)

for vent in vents:
    [x1,y1], [x2,y2] = list(map(int,x.split(',')) for x in vent.split(' -> '))
    # print(x1,y1,x2,y2)
    
    if x1 == x2:
        for i in range(y1,y2+[-1,1][y1<y2],[-1,1][y1<y2]):
            grid[x1 + i*width] +=1
    elif y1 == y2:
        for i in range(x1,x2+[-1,1][x1<x2],[-1,1][x1<x2]):
            # print(i,y1)
            grid[i + y1 * width]+=1
    else: 
        for a, b in zip(*[(i for i in range(x1,x2+[-1,1][x1<x2],[-1,1][x1<x2])),(j for j in range(y1,y2+[-1,1][y1<y2],[-1,1][y1<y2]))]):
        # for i in range(x1,x2+[-1,1][x1<x2],[-1,1][x1<x2]):    
        #     for j in range(y1,y2+[-1,1][y1<y2],[-1,1][y1<y2]):
            grid[a +b *width]+=1
print (len([x for x in grid if x>=2]))

# print(grid)