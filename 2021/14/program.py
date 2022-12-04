with open('input.txt') as file:
    seq, comps = file.read().split('\n\n')

polys ={}

dictionary = {}
def update(dictionary):
    newDict = dictionary.copy()
    for key, value in dictionary.items():
        reactanto = polys[key]
        newKey1 = key[0] + reactanto
        newKey2 = reactanto + key[1]
        newDict[newKey1] += value
        newDict[newKey2] += value
        newDict[key] -= value
    return newDict

from collections import Counter

for comp in comps.split('\n'):
    first, second = comp.split(' -> ')
    # second = comp.split(' -> ')[]
    polys[first]=second
    dictionary[first] = 0
for i in range(len(seq)-1):
    dictionary[seq[i:i+2]] +=1
# print(dictionary)
for _ in range(40):
    dictionary = update(dictionary)
numCounts = {'H':0,'B':0,'C':0,'N':0,'A':0,'Q':0,'W':0,'E':0,'R':0,'T':0,'Y':0,'U':0,'I':0,'O':0,'P':0,'S':0,'D':0,'F':0,'G':0,'J':0,'K':0,'L':0,'Z':0,'X':0,'V':0,'M':0}
for key, value in dictionary.items():# dictionary = update(dictionary)
    for k in numCounts:
        if k in key[0]:
            numCounts[k]+=value
print(numCounts)
print(numCounts['N']-numCounts['K']+1)
# print(dictionary)
exit()
seq = list(seq)
print(polys, seq)
# print([0,1,2][0:1])
def loop(seq):
    newSequence = [seq[0]]
    for i in range(len(seq)-1):
        # print(seq[i:i+2])
        reactant = ''.join(seq[i:i+2])
        # print(reactant)
        newAtom = polys[reactant]
        newSequence.append(newAtom)
        newSequence.append(seq[i+1])
    return newSequence
for i in range(40):
    print(i)
    seq = loop(seq).copy()
print(Counter(seq))