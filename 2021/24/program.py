with open('input.txt') as file:
    instructions = file.read().split('\n')
    # instructions = file.read().split('inp w\n')

for j in zip(i.split('\n') for i in instructions):
    print(j)
# print(instructions)
# exit()

def monad(instructions, inputValue):
    registers = {'w':0,'x':0,'y':0,'z':0}
    # w , x , y , z = 0,0,0,0
    for instruction in instructions:
        print('z=', registers['z'])
        typeOf = instruction.split()[0]

        if typeOf == 'inp':
            var = instruction.split()[1]
            inp = inputValue.pop(0)
            registers[var] = inp
        elif typeOf == 'add':
            var, var2 = instruction.split()[1:]
            try:
                var2 = int(var2)
            except ValueError:
                var2 = registers[var2]
            registers[var] = registers[var] + var2

        elif typeOf == 'mul':
            var, var2 = instruction.split()[1:]
            try:
                var2 = int(var2)
            except ValueError:
                var2 = registers[var2]
            registers[var] = registers[var] * var2
        elif typeOf == 'div':
            var, var2 = instruction.split()[1:]
            try:
                var2 = int(var2)
            except ValueError:
                var2 = registers[var2]
            registers[var] = registers[var] // var2
        elif typeOf == 'mod':
            var, var2 = instruction.split()[1:]
            try:
                var2 = int(var2)
            except ValueError:
                var2 = registers[var2]
            registers[var] = registers[var] % var2
        elif typeOf == 'eql':
            var, var2 = instruction.split()[1:]
            try:
                var2 = int(var2)
            except ValueError:
                var2 = registers[var2]
            registers[var] = int(registers[var] == var2)
    
    return registers

# for value in range(99999999999999,0, -1):
for value in range(11_111_111_111_111, 11111111111112):
# for value in range(17777777777773, 17777777777773+10):
    string = str(value)
    if '0' in string:
        continue
    ans = monad(instructions, list(map(int,list(string))))
    if ans['z'] == 0:
        print(value, ans)
        break
    print(value, ans)
    
# print(monad(instructions, [1,2,3,4]))