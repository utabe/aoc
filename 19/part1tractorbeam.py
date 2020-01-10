# --- Day 19: Tractor Beam ---
# Unsure of the state of Santa's ship, you borrowed the tractor beam technology from Triton. Time to test it out.
#
# When you're safely away from anything else, you activate the tractor beam, but nothing happens. It's hard to tell whether it's working if there's nothing to use it on. Fortunately, your ship's drone system can be configured to deploy a drone to specific coordinates and then check whether it's being pulled. There's even an Intcode program (your puzzle input) that gives you access to the drone system.
#
# The program uses two input instructions to request the X and Y position to which the drone should be deployed. Negative numbers are invalid and will confuse the drone; all numbers should be zero or positive.
#
# Then, the program will output whether the drone is stationary (0) or being pulled by something (1). For example, the coordinate X=0, Y=0 is directly in front of the tractor beam emitter, so the drone control program will always report 1 at that location.
#
# To better understand the tractor beam, it is important to get a good picture of the beam itself. For example, suppose you scan the 10x10 grid of points closest to the emitter:
#
#        X
#   0->      9
#  0#.........
#  |.#........
#  v..##......
#   ...###....
#   ....###...
# Y .....####.
#   ......####
#   ......####
#   .......###
#  9........##
# In this example, the number of points affected by the tractor beam in the 10x10 area closest to the emitter is 27.
#
# However, you'll need to scan a larger area to understand the shape of the beam. How many points are affected by the tractor beam in the 50x50 area closest to the emitter? (For each of X and Y, this will be 0 through 49.)

import sys
import collections
import itertools
# usage pyhon3 9.1.py program input
coords = list(itertools.chain(*sorted(list(set(itertools.permutations(list(range(0,51))*2,2))))))
# for coord in coords:
#     print(coord)
# exit()

initmem = list(map(int, open('input.in').read().split(',')))
# initmem = list(map(int, open(sys.argv[1]).read().split(',')))
mem = collections.defaultdict(lambda: 0, enumerate(initmem))
# print(initmem,mem)
# exit()
import time
beam_size = 0
def run(inp):
    global beam_size
    pc,base = 0, 0
    while mem[pc] != 99:
        opcode = mem[pc] % 100
        print(opcode)
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
            if op1 =='1':
                beam_size+=1
            # print(op1)
            # yield op1
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
grid = []
print('hi')
run(coords)
print('hello')
# for out in run([int(sys.argv[2])]):
    # print(out)
print(beam_size,'units')
