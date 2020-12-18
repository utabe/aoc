import re
inputs = open('input.in').read().split('\n')

# Part 1
pattern = re.compile('\([\d\+\*\s]+?\)')

def replace(replacee, replacer, range_=3):
    replacee = replacee[range_-1:]
    replacee[0] = replacer

    return replacee

def evaluate(expr):
    expr = ''.join(expr)
    while '(' in expr:
        expr = re.sub(pattern,str(evaluate(pattern.search(expr).group(0)[1:-1])),expr, count=1)
    expr = expr.split()

    while len(expr)>=3:
        evaluation = str(eval(' '.join(expr[:3])))
        expr = replace(expr,evaluation)

    return expr[0]

sum_ =0
for line in inputs:
    sum_ +=int(evaluate(list(line)))
print(sum_)

# Part 2
class MyNumber:
    def __init__(self, num):
        self.num = num
    def __sub__(self,other):
        return MyNumber(self.num * other.num)
    def __truediv__(self,other):
        return MyNumber(self.num + other.num)
    def __add__(self, other):
        return self.num + other
    __radd__ = __add__
    def __repr__(self):
        return f'MyNumber({self.num})'

sum2 = 0
for input_ in inputs:
    input_ = list(input_.replace('*','-').replace('+','/'))
    for i in range(len(input_)):
        if input_[i].isdigit():
            input_[i] = 'MyNumber('+input_[i]+')'
    sum2 += eval(''.join(input_))

print(sum2)

