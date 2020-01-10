# --- Part Two ---
# The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off. Since the air conditioner can't vent its heat anywhere but back into the spacecraft, it's actually making the air inside the ship warmer.
#
# Instead, you'll need to use the TEST to extend the thermal radiators. Fortunately, the diagnostic program (your puzzle input) is already equipped for this. Unfortunately, your Intcode computer is not.
#
# Your computer is only missing a few opcodes:
#
# Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
# Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
# Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
# Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
# Like all instructions, these instructions need to support parameter modes as described above.
#
# Normally, after an instruction is finished, the instruction pointer increases by the number of values in that instruction. However, if the instruction modifies the instruction pointer, that value is used and the instruction pointer is not automatically increased.
#
# For example, here are several programs that take one input, compare it to the value 8, and then produce one output:
#
# 3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
# 3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
# 3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
# 3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
# Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
#
# 3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
# 3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
# Here's a larger example:
#
# 3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
# The above example program uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.
#
# This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test, provide it 5, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one number, the diagnostic code.
#
# What is the diagnostic code for system ID 5?


import operator
import csv

csvFile = open('input.csv')
inputFile = csv.reader(csvFile)
Intcode = [*map(int,next(inputFile))]
# Test codes
# Intcode = [1,0,0,0,99]
# Intcode =[2,3,0,3,99]
# Intcode = [2,4,4,5,99,0]
# Intcode = [1,1,1,4,99,5,6,0,99]
# Intcode = [1101,100,-1,4,0]
# Intcode[1] = 12
# Intcode[2] = 2
# Intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
l = len(Intcode)
i=0
while i < l:
# for i in range(0,len(Intcode),4):
    # print(Intcode,i)
    code = Intcode[i]
    if code > 99:
        code = list(str(code))
        modes,code = code[:-2][::-1],code[-2:]
        modes = list(map(int,modes))
        code = int(''.join(code))
    else:
        modes= [0,0,0]
    modes += [0]
    # print(code, modes)
    if code == 1:
        op = operator.add
        first, second, store = Intcode[i+1:i+4]
        if modes[0] == 0:
            first = Intcode[first]
        if modes[1] == 0:
            second = Intcode[second]
        result = op(first, second)
        Intcode[store] = result
        i += 4
    elif code == 2:
        op = operator.mul
        first, second, store = Intcode[i+1:i+4]
        if modes[0] == 0:
            first = Intcode[first]
        if modes[1] == 0:
            second = Intcode[second]
        result = op(first, second)
        Intcode[store] = result
        i += 4
    elif code == 3:
        input3 = 5 # from instructions above
        store = Intcode[i+1]
        Intcode[store] =  input3
        i += 2
    elif code == 4:
        output = Intcode[i+1]
        if modes[0] == 0:
            print(Intcode[output]) # final print statement is the answer
        else:
            print(output)
        i += 2
    elif code == 5: #jump if true
        value = Intcode[i+1]
        position = Intcode[i+2]
        if modes[0] == 0:
            value = Intcode[value]
        if modes[1] == 0:
            position = Intcode[position]

        if value != 0:
            i = position
        else:
            i+=3

    elif code == 6: #jump if false
        value = Intcode[i+1]
        position = Intcode[i+2]
        if modes[0] == 0:
            value = Intcode[value]
        if modes[1] == 0:
            position = Intcode[position]

        if value == 0:
            i = position
        else:
            i+=3

    elif code == 7: #less than
        first, second, store = Intcode[i+1:i+4]
        if modes[0] == 0:
            first = Intcode[first]
        if modes[1] == 0:
            second = Intcode[second]

        if first < second:
            result = 1
        else:
            result = 0

        Intcode[store] = result
        i += 4

    elif code == 8: #equal to
        first, second, store = Intcode[i+1:i+4]
        if modes[0] == 0:
            first = Intcode[first]
        if modes[1] == 0:
            second = Intcode[second]

        if first == second:
            result = 1
        else:
            result = 0

        Intcode[store] = result
        i += 4

    elif code == 99:
        break
    else:
        raise ValueError

# print(Intcode)
csvFile.close()
