with open('input.txt') as file:
    lines = file.read().split()

print(lines)
def match(chL, chR):
    if chL == '[' and chR == ']':
        return True
    if chL == '(' and chR == ')':
        return True
    if chL == '{' and chR == '}':
        return True
    if chL == '<' and chR == '>':
        return True
    return False

points ={')':3,']':57, '}':1197, '>':25137}
scorePoints = {')':1,']':2,'}':3,'>':4}
reverseMatch ={ '(':')', '{':'}', '[':']', '<':'>'}
total = 0
pointTotals = []
for k, line in enumerate(lines):
    print('================', k)
    lst = []
    for char in line:
        # print(lst, char)
        if char in '([{<':
            lst.append(char)
        elif char in ')]}>':
            if match(lst[-1], char):
                lst.pop()
            else:
                print (lst, char,'corruption')
                total += points[char]
                break
    else:
        suffix = []
        for ch in lst[::-1]:
            suffix.append(reverseMatch[ch])
        p = 0
        for ch in suffix:
            p *=5
            p+= scorePoints[ch]
        pointTotals.append(p)
    # print(lst)
print(total)
print(sorted(pointTotals)[len(pointTotals)//2])