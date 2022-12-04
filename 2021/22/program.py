with open('example3.txt') as file:
    instructions = file.read().split('\n')

# print(instructions)

def parse(instruct):
    onOff, ranges = instruct.split()
    xRange, yRange, zRange = ranges.split(',')
    x1,x2 = xRange.split('=')[1].split('..')
    y1,y2 = yRange.split('=')[1].split('..')
    z1,z2 = zRange.split('=')[1].split('..')
    return onOff, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)

cuboid = {}
for i in instructions:
    # print(parse(i))
    onOff, x1, x2, y1, y2, z1, z2 = parse(i)
    for i in range(max(x1,-50), min(51, x2+1)):
        cuboid.setdefault(i, {})
        for j in range(max(y1,-50), min(51,y2+1)):
            cuboid[i].setdefault(j, {})
            for k in range(max(z1,-50), min(z2+1,51)):
                cuboid[i][j].setdefault(k, {})
                cuboid[i][j][k] = onOff
                
# print(cuboid)
print(str(cuboid).count('on'))
