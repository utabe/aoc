import numpy
count = [0,0,0,0,0,0,0,0,0,0,0,0]
with open('input.txt') as f:
    a=0
    for line in f.readlines():
        a+=1
        for index, val in enumerate(line):
            if val == '1':
                count[index] +=1

print(a)
gamma = 0b001110101111
epsilon = 0b110001010000
print(gamma * epsilon)
print(count)

with open('input.txt') as f:
    lines = f.readlines()

ox = lines[:]
co2 = lines[:]
def findCommon(pos, lst, mode="ox"):
    cnt = 0
    if len(lst)==1:
        return lst
    for i in lst:
        if i[pos]=='1':
            cnt +=1
    if mode == "ox":
        print(float(cnt)/len(lst))
        if float(cnt)/len(lst) >= 0.5:
            ans = '1'
        else:
            ans = '0'
    else:
        if float(cnt)/len(lst) < 0.5:
            ans = '1'
        else:
            ans = '0'
    print(len([x for x in lst if x[pos]==ans]))
    # exit()
    return [x for x in lst if x[pos]==ans]

for indexI in range(len(ox[0])):
    # answer=''//
    # while len(ox) >1:
    print(len(ox))
    ox = findCommon(indexI, ox, mode="ox")
for indexI in range(len(co2[0])):
    print(len(co2),'hi')
    # exit()
    # answer=''//
    # while len(ox) >1:
    co2 = findCommon(indexI, co2, mode="co2")

    
print("px",ox)
print("co2",co2)
print(int(ox[0][:-1],2))
print(int(co2[0][:-1],2))
print(int(ox[0][:-1],2)*int(co2[0],2))
