with open('example.txt') as file:
    lines = file.read().split('\n')
total=0
for line in lines:
    print(line)
    l1,l2 = line.split(',')
    i1,i2 = map(int,l1.split('-'))
    j1,j2 = map(int,l2.split('-'))
    set1 = set(range(i1,i2+1))
    set2 = set(range(j1,j2+1))
    set3 = set1 & set2
    if len(set3):
        total+=1
    # if set3 == set1 or set3==set2:
    #     total +=1
print(total)