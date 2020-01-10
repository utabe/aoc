#!python3
import program
import sys
from intcode import IntCode
from itertools import combinations

assert len(sys.argv) == 2

code = open(sys.argv[1]).read().strip().split(',')
data = list(map(int, code))


processor = IntCode(0, data, "X")

instr_str = "east\n"+"east\n"+"take semiconductor\n"+"north\n"+"take planetoid\n"+"north\n"+"take antenna\n"+"south\n"+"west\n"+"take food ration\n"+"west\n"+"west\n"+"take monolith\n"+"east\n"+"east\n"+"north\n"+"take space law space brochure\n"+"east\n"+"take jam\n"+"west\n"+"north\n"+"north\n"+"take weather machine\n"+"south\n"+"south\n"+"south\n"+"east\n"+"south\n"+"east\n"+"south\n"+"south\n"+"east\n"+"east\n"
# all combinations of equipment

inventory = ["food ration", "weather machine", "antenna", "space law space brochure", "jam", "semiconductor", "planetoid", "monolith"]

for i in range(len(inventory)+1):
    for comb in combinations(inventory, i):
        # drop everything
        for inv in inventory:
            instr_str += "drop "+inv+"\n"
        for item in comb:
            instr_str += "take "+item+"\n"
        instr_str += "east\n"


instr = (list(map(ord, instr_str)))

# combin

for i in instr:
    processor.manualio.append(i)


while 1:
    processor.run_intcode()
