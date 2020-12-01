# --- Part Two ---
# It's no good - in this configuration, the amplifiers can't generate a large enough output signal to produce the thrust you'll need. The Elves quickly talk you through rewiring the amplifiers into a feedback loop:
#
#       O-------O  O-------O  O-------O  O-------O  O-------O
# 0 -+->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-.
#    |  O-------O  O-------O  O-------O  O-------O  O-------O |
#    |                                                        |
#    '--------------------------------------------------------+
#                                                             |
#                                                             v
#                                                      (to thrusters)
# Most of the amplifiers are connected as they were before; amplifier A's output is connected to amplifier B's input, and so on. However, the output from amplifier E is now connected into amplifier A's input. This creates the feedback loop: the signal will be sent through the amplifiers many times.
#
# In feedback loop mode, the amplifiers need totally different phase settings: integers from 5 to 9, again each used exactly once. These settings will cause the Amplifier Controller Software to repeatedly take input and produce output many times before halting. Provide each amplifier its phase setting at its first input instruction; all further input/output instructions are for signals.
#
# Don't restart the Amplifier Controller Software on any amplifier during this process. Each one should continue receiving and sending signals until it halts.
#
# All signals sent or received in this process will be between pairs of amplifiers except the very first signal and the very last signal. To start the process, a 0 signal is sent to amplifier A's input exactly once.
#
# Eventually, the software on the amplifiers will halt after they have processed the final loop. When this happens, the last output signal from amplifier E is sent to the thrusters. Your job is to find the largest output signal that can be sent to the thrusters using the new phase settings and feedback loop arrangement.
#
# Here are some example programs:
#
# Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):
#
# 3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
# 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
# Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):
#
# 3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
# Try every combination of the new phase settings on the amplifier feedback loop. What is the highest signal that can be sent to the thrusters?



import operator
import csv
import itertools

phases = itertools.permutations([0,1,2,3,4])

csvFile = open('input.csv')
inputFile = csv.reader(csvFile)
Intcode = [*map(int,next(inputFile))]
originalIntcode = Intcode.copy()
# Test codes
# Intcode = [1,0,0,0,99]
# Intcode =[2,3,0,3,99]
# Intcode = [2,4,4,5,99,0]
# Intcode = [1,1,1,4,99,5,6,0,99]
# Intcode = [1101,100,-1,4,0]
# Intcode[1] = 12
# Intcode[2] = 2
# Intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
# Intcode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
amps = [Intcode.copy() for i in range(5)]
gotPhaseInput = [False] * 5
print(gotPhaseInput)
exit()
currentAmp = 0
l = len(Intcode)
maxAmp = 0
for phase in phases:
    firstCodes = {0:0,1:phase[0],2:phase[1],3:phase[2],4:phase[3],5:phase[4]}
    ampInput = 0
    print(phase )
    stillProcessing = True
    counter = 0
    while stillProcessing:
    # for phaseInput in phase:
        i=0
        input3 = [phaseInput, ampInput]
        # Intcode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        Intcode = amps[currentAmp]
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
                store = Intcode[i+1]
                Intcode[store] =  input3.pop(0)
                print('intcode[store]', Intcode[store])
                i += 2
            elif code == 4:
                output = Intcode[i+1]
                if modes[0] == 0:
                    print(Intcode[output]) # final print statement is the answer
                    ampInput = Intcode[output]
                else:
                    print(output)
                    ampInput = output
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
                stillProcessing = False
                break
            else:
                raise ValueError
        if currentAmp == 4:
            currentAmp = 0
        else:
            currentAmp += 1
        maxAmp = max(maxAmp, ampInput)
        counter +=1
print(maxAmp)
# print(Intcode)
csvFile.close()
