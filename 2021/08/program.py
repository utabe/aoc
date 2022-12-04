with open('input.txt') as file:
    times = file.read().split('\n')
times = list(t.split(' | ') for t in times)
# print(times)
count =0
for time in times:
    for t in time[1].split():
        l = len(t)
        if l == 2 or l == 3 or l == 4 or l == 7:
            count +=1
print(count)

# digitLetters = {
#     0: 'a b c e f g'.split(),
#     1: 'c f'.split(),
#     2: 'a c d e g'.split(),
#     3: 'a c d f g'.split(),
#     4: 'b c d f'.split(),
#     5: 'a b d f g'.split(),
#     6: 'a b d e f g'.split(),
#     7: 'a c f'.split(),
#     8: 'a b c d e f g'.split(),
#     9: 'a b c d f g'.split(),
#     'f': 9 #only number 2 missing it
#     'c': only 5 and 6 missing it
#     'a': only 1 and 4 missing it
#     start with digit 1, the two letter, number 2 is the one missing one of the numbers, 5 and 6 are the ones missing the other
#     the one with 4 enclosed is 9
#     the last one missing two numbers is 3
#     the last one is 0
# }
SUM = 0
def findLetters(text):
    #find the 1
    global l1
    l1 = [l for l in text if len(l)==2][0]
    text.remove(l1)
    l1=list(l1)
    #find the 7
    global l7
    l7 = [l for l in text if len(l)==3][0]
    text.remove(l7)
    l7=list(l7)
    #find the 4
    global l4
    l4 = [l for l in text if len(l)==4][0]
    text.remove(l4)
    l4=list(l4)
    #find the 8
    global l8
    l8 = [l for l in text if len(l)==7][0]
    text.remove(l8)
    l8=list(l8)
    #find the 9
    global l9
    l9 = [l for l in text if all(a in l for a in l4)][0]
    # print(l9, 'l9', text, l9 in text, 'cbdgef')
    text.remove(l9)
    l9 = list(l9)
    #find the 3
    global l3
    l3 = [l for l in text if all(a in l for a in l1)and len(l)==5][0]
    text.remove(l3)
    l3 = list(l3)
    #find the 0
    global l0
    l0 = [l for l in text if all(a in l for a in l1)][0]
    text.remove(l0)
    l0 = list(l0)
    #find the 6
    global l6
    l6 = [l for l in text if len(l)==6][0]
    text.remove(l6)
    l6 = list(l6)
    #find the 5
    global l5
    l5 = [l for l in text if all(j in l6 for j in l)][0]
    text.remove(l5)
    l5 = list(l5)
    #find the 2
    global l2
    l2 = list(text[0])
    
for time in times:
    findLetters(time[0].split())
    num = ''
    for t in time[1].split():
        if sorted(t) == sorted(''.join(l0)):
            num +='0'
        if sorted(t) == sorted(''.join(l1)):
            num +='1'
        if sorted(t) == sorted(''.join(l2)):
            num +='2'
        if sorted(t) == sorted(''.join(l3)):
            num +='3'
        if sorted(t) == sorted(''.join(l4)):
            num +='4'
        if sorted(t) == sorted(''.join(l5)):
            num +='5'
        if sorted(t) == sorted(''.join(l6)):
            num +='6'
        if sorted(t) == sorted(''.join(l7)):
            num +='7'
        if sorted(t) == sorted(''.join(l8)):
            num +='8'
        if sorted(t) == sorted(''.join(l9)):
            num +='9'
    print(num,'num')
    SUM += int(num)

   

print(SUM)
