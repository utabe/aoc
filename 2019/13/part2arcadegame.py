# --- Part Two ---
# The game didn't run because you didn't put in any quarters. Unfortunately, you did not bring any quarters. Memory address 0 represents the number of quarters that have been inserted; set it to 2 to play for free.
#
# The arcade cabinet has a joystick that can move left and right. The software reads the position of the joystick with input instructions:
#
# If the joystick is in the neutral position, provide 0.
# If the joystick is tilted to the left, provide -1.
# If the joystick is tilted to the right, provide 1.
# The arcade cabinet also has a segment display capable of showing a single number that represents the player's current score. When three output instructions specify X=-1, Y=0, the third output instruction is not a tile; the value instead specifies the new score to show in the segment display. For example, a sequence of output values like -1,0,12345 would show 12345 as the player's current score.
#
# Beat the game by breaking all the blocks. What is your score after the last block is broken?


import sys
import collections
# usage pyhon3 9.1.py program input
counter = 0
screen = []
def run(inp):
    global counter
    global screen
    initmem = list(map(int, open('input.txt').read().split(',')))
    # initmem = list(map(int, open(sys.argv[1]).read().split(',')))
    mem = collections.defaultdict(lambda: 0, enumerate(initmem))
    mem[0] = 2
    pc,base = 0, 0
    while mem[pc] != 99:
        opcode = mem[pc] % 100
        modes = ("%05d" % mem[pc])[0:3]
        o1 = base if modes[2] == '2' else 0
        o2 = base if modes[1] == '2' else 0
        o3 = base if modes[0] == '2' else 0
        if opcode in (1,2,3,4,5,6,7,8,9):
            op1 = mem[pc+1] if modes[2] == '1' else mem[o1+mem[pc+1]]
        if opcode in (1,2,5,6,7,8):
            op2 = mem[pc+2] if modes[1] == '1' else mem[o2+mem[pc+2]]
        if opcode in (1,2): # add and mul
            f = {1: int.__add__, 2: int.__mul__}[opcode]
            mem[o3+mem[pc+3]] = f(op1,op2)
            pc += 4
        elif opcode == 3: # input
            mem[o1+mem[pc+1]] = inp.pop(0)
            pc += 2
        elif opcode  == 4: # output
            pc += 2
            screen.append(op1)
            yield op1
        elif opcode == 5: # jump if true
            pc = op2 if op1 != 0 else pc+3
        elif opcode == 6: # jump if false
            pc = op2 if op1 == 0 else pc+3
        elif opcode == 7: # less than
            mem[o3+mem[pc+3]] = 1 if op1 < op2 else 0
            pc += 4
        elif opcode == 8: # equals
            mem[o3+mem[pc+3]] = 1 if op1 == op2 else 0
            pc += 4
        elif opcode == 9: # set relative base
            base += op1
            pc += 2
        else: raise Exception("invalid opcode %d" % opcode)

for out in run([int(sys.argv[1])]):
# for out in run([int(sys.argv[2])]):
    print(screen)
