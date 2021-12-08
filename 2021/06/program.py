lanternfish = [8]
# for _ in range(128):
#     newFish = 0
#     for i in range(len(lanternfish)):
#         if lanternfish[i] == 0:
#             lanternfish[i] = 6
#             newFish +=1
#         else:
#             lanternfish[i] -=1
#     lanternfish += [8]*newFish
    # print(len(lanternfish))
# print(len(lanternfish))
# 1 at 80 = 1401
# 2 at 80 = 1191
# 3 at 80 = 1054
# 4 at 80 = 1034
# 5 at 80 = 950
rate80 = {'1':1401,'2':1191,'3':1154,'4':1034,"5":950}
from collections import Counter
# counts = Counter(lanternfish)
# print(counts)
# rate 128
# 8 = 49380
#  7= 51564
# 6 58016
# 5 62475
# 4 67616
# 3 75638
# 2 79321
# 1 90763
# 0 94508
counts0 = {5: 19464, 0: 12888, 3: 12481, 2: 11593, 7: 11442, 4: 8824, 6: 7428, 1: 6643, 8: 3745}
counts1 = {'6': 19464, '1': 12888, '4': 12481, '3': 11593, '8': 11442, '5': 8824, '2': 6643, '0': 3745, '7': 3683}
counts2= {'2': 12888, '5': 12481, '4': 11593, '0': 11442, '6': 8824, '7': 8022, '3': 6643, '1': 3745, '8': 3683}
counts3 = {'3': 12888, '6': 12481, '5': 11593, '1': 11442, '8': 8022, '4': 6643, '7': 5141, '2': 3745, '0': 3683}
counts4 = {'4': 12888, '6': 11593, '2': 11442, '0': 8022, '5': 6643, '8': 5141, '7': 4459, '3': 3745, '1': 3683}
counts5 ={'5': 12888, '3': 11442, '1': 8022, '6': 6643, '7': 6452, '0': 5141, '8': 4459, '4': 3745, '2': 3683}
counts6 = {'6': 12888, '4': 11442, '2': 8022, '8': 6452, '1': 5141, '0': 4459, '5': 3745, '3': 3683, '7': 2184}
counts7 = {'5': 11442, '3': 8022, '0': 6452, '7': 6436, '2': 5141, '1': 4459, '6': 3745, '4': 3683, '8': 2184}
counts8 = {'6': 11442, '4': 8022, '1': 6452, '8': 6436, '3': 5141, '2': 4459, '5': 3683, '0': 2184, '7': 1561}
rate128 = {'0':94508,'1':90763,'2':79321,'3':75638,'4':67616,'5':62475,'6':58016,'7':51564,'8':49380}
# with open('input.txt') as file:
#     fishies = file.readline().split(',')
# fishCount = Counter(fishies)
fishCount = {'1': 79, '5': 71, '4': 56, '3': 52, '2': 42}
total =0
# for i in '1 2 3 4 5'.split():
#     fishCount[i] * 
total += sum(rate128[k] *v for k,v in counts1.items()) * fishCount['1']
total += sum(rate128[k] *v for k,v in counts2.items()) * fishCount['2']
total += sum(rate128[k] *v for k,v in counts3.items()) * fishCount['3']
total += sum(rate128[k] *v for k,v in counts4.items()) * fishCount['4']
total += sum(rate128[k] *v for k,v in counts5.items()) * fishCount['5']
# print(sum(rate80[fish]for fish in fishies))    
print(total)