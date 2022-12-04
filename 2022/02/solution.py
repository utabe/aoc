with open('input.txt') as file:
    lines = file.readlines()
print(lines)
total =0
# for line in lines:
#     if line == 'A X\n':
#         total+=4
#     if line == 'A Y\n':
#         total+=8
#     if line == 'A Z\n':
#         total+=3
#     if line == 'B X\n':
#         total+=1
#     if line == 'B Y\n':
#         total+=5
#     if line == 'B Z\n':
#         total+=9
#     if line == 'C X\n':
#         total+=7
#     if line == 'C Y\n':
#         total+=2
#     if line == 'C Z\n':
#         total+=6
for line in lines:
    if line == 'A X\n':
        total+=3
    if line == 'A Y\n':
        total+=4
    if line == 'A Z\n':
        total+=8
    if line == 'B X\n':
        total+=1
    if line == 'B Y\n':
        total+=5
    if line == 'B Z\n':
        total+=9
    if line == 'C X\n':
        total+=2
    if line == 'C Y\n':
        total+=6
    if line == 'C Z\n':
        total+=7
print(total)