# --- Day 10: Monitoring Station ---
# You fly into the asteroid belt and reach the Ceres monitoring station. The Elves here have an emergency: they're having trouble tracking all of the asteroids and can't be sure they're safe.
#
# The Elves would like to build a new monitoring station in a nearby area of space; they hand you a map of all of the asteroids in that region (your puzzle input).
#
# The map indicates whether each position is empty (.) or contains an asteroid (#). The asteroids are much smaller than they appear on the map, and every asteroid is exactly in the center of its marked position. The asteroids can be described with X,Y coordinates where X is the distance from the left edge and Y is the distance from the top edge (so the top-left corner is 0,0 and the position immediately to its right is 1,0).
#
# Your job is to figure out which asteroid would be the best place to build a new monitoring station. A monitoring station can detect any asteroid to which it has direct line of sight - that is, there cannot be another asteroid exactly between them. This line of sight can be at any angle, not just lines aligned to the grid or diagonally. The best location is the asteroid that can detect the largest number of other asteroids.
#
# For example, consider the following map:
#
# .#..#
# .....
# #####
# ....#
# ...##
# The best location for a new monitoring station on this map is the highlighted asteroid at 3,4 because it can detect 8 asteroids, more than any other location. (The only asteroid it cannot detect is the one at 1,0; its view of this asteroid is blocked by the asteroid at 2,2.) All other asteroids are worse locations; they can detect 7 or fewer other asteroids. Here is the number of other asteroids a monitoring station on each asteroid could detect:
#
# .7..7
# .....
# 67775
# ....7
# ...87
# Here is an asteroid (#) and some examples of the ways its line of sight might be blocked. If there were another asteroid at the location of a capital letter, the locations marked with the corresponding lowercase letter would be blocked and could not be detected:
#
# #.........
# ...A......
# ...B..a...
# .EDCG....a
# ..F.c.b...
# .....c....
# ..efd.c.gb
# .......c..
# ....f...c.
# ...e..d..c
# Here are some larger examples:
#
# Best is 5,8 with 33 other asteroids detected:
#
# ......#.#.
# #..#.#....
# ..#######.
# .#.#.###..
# .#..#.....
# ..#....#.#
# #..#....#.
# .##.#..###
# ##...#..#.
# .#....####
# Best is 1,2 with 35 other asteroids detected:
#
# #.#...#.#.
# .###....#.
# .#....#...
# ##.#.#.#.#
# ....#.#.#.
# .##..###.#
# ..#...##..
# ..##....##
# ......#...
# .####.###.
# Best is 6,3 with 41 other asteroids detected:
#
# .#..#..###
# ####.###.#
# ....###.#.
# ..###.##.#
# ##.##.#.#.
# ....###..#
# ..#.#..#.#
# #..#.#.###
# .##...##.#
# .....#.#..
# Best is 11,13 with 210 other asteroids detected:
#
# .#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##
# Find the best location for a new monitoring station. How many other asteroids can be detected from that location?

from fractions import Fraction
import itertools

file = open('asteroidfield.txt')
field = file.readlines()
# field ='''......#.#.
# #..#.#....
# ..#######.
# .#.#.###..
# .#..#.....
# ..#....#.#
# #..#....#.
# .##.#..###
# ##...#..#.
# .#....####'''.split()
print(field)
height = len(field)
width = len(field[0])
print(height,width)
checked = []
filtered = []
for i,j in itertools.combinations_with_replacement(range(1,max(width,height)),2):
    if j == 0:continue
    if Fraction(i,j) not in checked:
        checked.append(Fraction(i,j))
        filtered.append([i,j])
def add(coor1,coor2):
    return [coor1[0]+coor2[0],coor1[1]+coor2[1]]
for coor in filtered[:]:
    filtered.append(coor[::-1])
filtered.append([1,0])
filtered.append([0,1])
filtered = filtered[1:]
for coor in filtered[:]:
    for addon in [[1,1],[1,-1],[-1,1],[-1,-1]]:
        a = [coor[0]*addon[0],coor[1]*addon[1]]
        if a not in filtered:
            filtered.append(a)
# print(*filtered,sep='\n')
# exit()
maxAsteroids = 0
bestSpot = [-1,-1]
for y in range(height):
    for x in range(width):
        if field[y][x] == '#':
            totalAsteroidsSeen = 0
            station = [x, y]
            # print(station)
            for coor in filtered:
                current = station.copy()
                while current[0] >=0 and current[0]<width and current[1]>=0 and current[1] <height:
                        current = add(current, coor)
                        # print(field[current[y]][current[x]])
                        # print(station,current,coor,totalAsteroidsSeen)
                        # print(current[0] >=0 and current[0]<=width and current[1]>=0 and current[1] <=height)
                        # import pdb; pdb.set_trace()
                        if current[0]<0 or current[1]<0:
                            break
                        try:
                            if field[current[1]][current[0]] =='#':
                                # print(current[1],current[0])
                                totalAsteroidsSeen+=1
                                break
                        except:
                            pass
            # print(totalAsteroidsSeen,station)
            if totalAsteroidsSeen > maxAsteroids:
                maxAsteroids = totalAsteroidsSeen
                bestSpot = [x,y]
print(bestSpot,maxAsteroids) #[11,13] with 227 asteroids
