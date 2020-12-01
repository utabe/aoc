import numpy as np
with open('input.in') as input_file:
    inpstring = input_file.readlines()

inpstring = inpstring[0].strip()
# inpstring = ['19617804207202209144916044189917']
inparray = np.array([int(ele) for ele in inpstring])

thepattern = [0,1,0,-1]
Niters = 100
newinparray = np.copy(inparray)
for iteration in range(Niters):
    newpattern = []
    for ichar in range(len(newinparray)):
        outpattern = []
        for ipattern in range(4):
            outpattern += [thepattern[ipattern]]*(ichar+1)
        if len(outpattern) < len(newinparray):
            scale = len(newinparray)//len(outpattern) + 1
            outpattern = outpattern * scale
        outpattern = outpattern[1:len(newinparray)+1]
        newpattern.append(np.abs(np.sum(np.array(outpattern) * newinparray)) % 10)
    newinparray = np.array([int(ele) for ele in newpattern])

print(newinparray[0:8])

inparray = np.array([int(ele) for ele in inpstring]*10000)
theoffset = int(inpstring[0:7])

# at that distance, it's literally *just* a sum and nothing else

Niters = 100
newinparray = np.copy(inparray)
newinparray = newinparray[theoffset:]
for iteration in range(Niters):
    newpattern = np.cumsum(newinparray[::-1]) % 10
    newinparray = newpattern[::-1]

print(newinparray[0:8])
