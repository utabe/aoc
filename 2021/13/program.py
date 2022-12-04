with open('input.txt') as file:
    pts, flds = file.read().split('\n\n')

points = set(tuple(map(int, pt.split(','))) for pt in pts.split('\n'))
folds = flds.split('\n')
print(points, folds)

for fold in folds:
    axis = int(fold.split('=')[1])
    for pnt in points.copy():
        x = pnt[0]
        y = pnt[1]
        if 'x' in fold:
            if pnt[0] > axis:
                diff = x - axis
                newX = x - 2*diff
                points.add(tuple([newX, y]))
                points.remove(pnt)
        else:
            if pnt[1] > axis:
                diff = y - axis
                newY = y - 2*diff
                points.add(tuple([x, newY]))
                points.remove(pnt)
print(len(points))
for y in range(7):
    for x in range(50):
        if (x,y) in points:
            print('#',end='')
        else:
            print('.',end='')
    print()
