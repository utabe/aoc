# --- Part Two ---
# It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.
#
# To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.
#
# The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:
#
# ...........
# .+-----+...
# .|.....|...
# .|..+--X-+.
# .|..|..|.|.
# .|.-X--+.|.
# .|..|....|.
# .|.......|.
# .o-------+.
# ...........
# In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.
#
# However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.
#
# Here are the best steps for the extra examples from above:
#
# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
# What is the fewest combined steps the wires must take to reach an intersection?


import csv

file = open('input.txt')
csv_reader = csv.reader(file)

wire1 = next(csv_reader)
wire2 = next(csv_reader)

def add_path(path, stop):
    dir = stop[0]
    if dir=='R':
        a=1+0j
    elif dir=='L':
        a=-1+0j
    elif dir =='U':
        a=0+1j
    elif dir == 'D':
        a=0-1j
    else:
        raise ValueError

    for i in range(int(stop[1:])):
        path.append(path[-1]+a)

    return path

path1 = [0+0j]
path2 = [0+0j]
# stop = 'R30'
for stop in wire1:
    add_path(path1, stop)
for stop in wire2:
    add_path(path2, stop)
# print(path1, path2)
path1=path1[1:]
path2=path2[1:]
mini =100000

for stop in range(len(path1)):
    t = path1[stop]
    if t in path2:
        mini = min(mini, stop+path2.index(t))

print(mini +2) #Because we removed the first to elements of the path earlier
file.close()
