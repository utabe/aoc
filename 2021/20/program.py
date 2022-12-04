import copy
with open('example.txt') as file:
    algorithm = file.readline()
    file.readline()
    data = [list(x.replace('\n', '')) for x in file.readlines()]

# print(algorithm)
def printt(datum):
    for d in datum:
        print(d)



data = [['.']+x+['.'] for x in data]
data = [['.']+x+['.'] for x in data]
data = [['.']+x+['.'] for x in data]
data = [['.']+x+['.'] for x in data]
data = [['.']+x+['.'] for x in data]
data = [['.']+x+['.'] for x in data]
width = len(data[0])

data = [['.']*(width)] + data + [['.']*(width)]
data = [['.']*(width)] + data + [['.']*(width)]
data = [['.']*(width)] + data + [['.']*(width)]
data = [['.']*(width)] + data + [['.']*(width)]
data = [['.']*(width)] + data + [['.']*(width)]
data = [['.']*(width)] + data + [['.']*(width)]
height = len(data)

printt(data)
print('================================')
def kernalize(x,y,filler):
    kernalNum = ''
    for j in [-1,0,1]:
        for i in [-1,0,1]:
            if x+i < 0 or x+i >= width or y+j < 0 or y+j >= width:
                kernalNum += filler
            else:
                # print(width, height)
                # print("x:",x,'Y:',y,'i',i,'J:',j)
                kernalNum += data[y+j][x+i]
    return kernalNum

starterBuffer =  []
for i in range(height):

    starterBuffer.append(list('.'*(width)))
newImageBuffer = copy.deepcopy(starterBuffer)

# printt(newImageBuffer/)
print(len(algorithm),'alg')

    
def loop(filler):
    for y in range(height):
        for x in range(width):
            # print("x:",x, "y:",y)
            # print('h:',height,"w:",width)
            kern = kernalize(x,y,filler)
            kern = kern.replace('.','0').replace('#','1')
            kern = int(kern,2)
            # print(kern, algorithm[kern])
            newImageBuffer[y][x] = algorithm[kern]
            # printt(newImageBuffer)
            # if x==3 and y==3:
            #     quit()
            
    return newImageBuffer

data = copy.deepcopy(loop('.'))
height = len(data)
width = len(data[0])
# data = [['#']+x+['#'] for x in data]

# data = [['#']*(width)] + data + [['#']*(width)]

printt(data)
starterBuffer =  []
for i in range(height):

    starterBuffer.append(list('.'*(width)))
newImageBuffer = copy.deepcopy(starterBuffer)

print('========================')
data = copy.deepcopy(loop('.'))
# printt(data)

print(sum(y == '#' for x in data for y in x))


