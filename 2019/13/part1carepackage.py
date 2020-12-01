# --- Day 13: Care Package ---
# As you ponder the solitude of space and the ever-increasing three-hour roundtrip for messages between you and Earth, you notice that the Space Mail Indicator Light is blinking. To help keep you sane, the Elves have sent you a care package.
#
# It's a new game for the ship's arcade cabinet! Unfortunately, the arcade is all the way on the other end of the ship. Surely, it won't be hard to build your own - the care package even comes with schematics.
#
# The arcade cabinet runs Intcode software like the game the Elves sent (your puzzle input). It has a primitive screen capable of drawing square tiles on a grid. The software draws tiles to the screen with output instructions: every three output instructions specify the x position (distance from the left), y position (distance from the top), and tile id. The tile id is interpreted as follows:
#
# 0 is an empty tile. No game object appears in this tile.
# 1 is a wall tile. Walls are indestructible barriers.
# 2 is a block tile. Blocks can be broken by the ball.
# 3 is a horizontal paddle tile. The paddle is indestructible.
# 4 is a ball tile. The ball moves diagonally and bounces off objects.
# For example, a sequence of output values like 1,2,3,6,5,4 would draw a horizontal paddle tile (1 tile from the left and 2 tiles from the top) and a ball tile (6 tiles from the left and 5 tiles from the top).
#
# Start the game. How many block tiles are on the screen when the game exits?


import sys
import collections
# usage pyhon3 9.1.py program input
counter = 0
block_total = 0
def run(inp):
    global counter
    global block_total
    initmem = list(map(int, open('input.txt').read().split(',')))
    # initmem = list(map(int, open(sys.argv[1]).read().split(',')))
    mem = collections.defaultdict(lambda: 0, enumerate(initmem))
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
            counter+=1
            if counter%3==0:
                if op1 == 2:
                    block_total+=1
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
    print(out)
    print(block_total,'blocks')
