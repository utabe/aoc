with open('input.txt') as file:
    lines = file.read()

elves = lines.split('\n\n')

elves = [sum(list(map(int,elf.split('\n')))) for elf in elves]
max1 = max(elves)
print('max1',max1)
elves.remove( max1)
max2 = max(elves)
print('max2',max2)
elves.remove( max2)
max3 = max(elves)
print('max3',max3)
elves.remove( max3)
print(max1+max2+max3)