from operator import itemgetter
from itertools import groupby

adapters = list(map(int, open('input.in').read().split('\n')))
adapters.sort()
adapters = [0]+adapters+[adapters[-1]+3]
all_adapters = set(adapters)
print(adapters)
ones = 0
threes = 0
needed=set([0,adapters[-1]])

for i in range(1,len(adapters)):
    diff = adapters[i]-adapters[i-1]
    if diff == 1:
        ones +=1
    elif diff == 3:
        # print(adapters[i-1], adapters[i])
        needed.add(adapters[i-1])
        needed.add(adapters[i])
        threes +=1
print('Part1',ones * threes, ones, threes)

# print(needed, all_adapters, all_adapters-needed)
optionals = sorted(list(all_adapters-needed))
#one-liner from Stackoverflow to split list when consecutive entrees are greater than 1 apart
split = [list(map(itemgetter(1), g)) for k, g in groupby(enumerate(optionals), lambda x: x[0]-x[1])]

total = 1
for i in split:
    if len(i)==3:
        total *=7  #7 possible ways to get between two needed adapters with 3 adapters inbetween
    else:
        total *= (2**(len(i)))
print(total)


# 0,1,f           1 = 2^0
# 0,1,2,f         2 = 2 ^1
# 0,1,2,3,f       4 = 2 ^2
# 0,1,2,3,4,f     7