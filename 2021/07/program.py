with open('input.txt') as file:
    numbers = list(map(int,file.readline().split(',')))

print(numbers)
print(sum(numbers)/len(numbers))
a = 1
for i in numbers:
    if i!=0:
        a *= i
# print(a**(1/len(numbers)))
print(a)
print(len(numbers))
print(max(numbers),min(numbers))

def difftoNum(num, nums):
    a = 0
    for n in nums:
        a += abs(n-num)
    return a

def difftoNum2(num, nums):
    a = 0
    for n in nums:
        d = abs(n-num)
        a += d*(d + 1) / 2
    return a
for i in range(min(numbers),800):
    print(i,difftoNum2(i, numbers))