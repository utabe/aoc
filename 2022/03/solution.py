with open('input.txt') as file:
    lines = file.readlines()
total =0
# for line in lines:
#     set1 = set(line[:(len(line)-1)//2])
#     set2 = set(line[(len(line)-1)//2:-1])
#     intersection = (set1&set2).pop()
for i in range(0,len(lines),3):
    set1 = set(lines[i])
    set2 = set(lines[i+1])
    set3 = set(lines[i+2])
    intersection = (set1&set2&set3 -{'\n'}).pop()
    if intersection in 'qwertyuiopasdfghjklzxcvbnm':
        total += ord(intersection)-96
    else:
        total += ord(intersection)-64+26

print(set1,set2, intersection, total)