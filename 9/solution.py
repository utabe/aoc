import sys
import collections


def run(inp):
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
