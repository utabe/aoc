example = 'target area: x=20..30, y=-10..-5'
inputt = 'target area: x=244..303, y=-91..-54'

xmin = 244
xmax = 303
ymin = -91
ymax = -54

useExample = False
if useExample:
    xmin = 20
    xmax = 30
    ymin = -10
    ymax = -5

import math
def cycle(xVel, yVel, xPos, yPos):
    xPos += xVel
    yPos += yVel
    # print('xVel before',xVel)
    if xVel != 0:
        xVel -= math.copysign(1, xVel)
    # print('xvel after', xVel)
    yVel -= 1
    return xVel, yVel, xPos, yPos
bestCount = []
bestHeight=[]
for startXv in range(500):
    for startYv in range(-500,700):
        xVel = startXv
        yVel = startYv
        xPos = 0
        yPos = 0
        counter = 0
        maxHeight = 0
        while xPos < xmax and yPos > ymin:
            xVel, yVel, xPos, yPos = cycle(xVel, yVel, xPos, yPos)
            maxHeight = max(maxHeight, yPos)
            if xPos <= xmax and xPos >= xmin and yPos >= ymin and yPos <= ymax:
                #we're in
                # print('we in with starting speed', startXv, startYv, 'and max height',maxHeight)
                bestHeight.append(maxHeight)
                break


print(len(bestHeight))
