# --- Part Two ---
# Now, you just need to figure out how many orbital transfers you (YOU) need to take to get to Santa (SAN).
#
# You start at the object YOU are orbiting; your destination is the object SAN is orbiting. An orbital transfer lets you move from any object to an object orbiting or orbited by that object.
#
# For example, suppose you have the following map:
#
# COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN
# Visually, the above map of orbits looks like this:
#
#                           YOU
#                          /
#         G - H       J - K - L
#        /           /
# COM - B - C - D - E - F
#                \
#                 I - SAN
# In this example, YOU are in orbit around K, and SAN is in orbit around I. To move from K to I, a minimum of 4 orbital transfers are required:
#
# K to J
# J to E
# E to D
# D to I
# Afterward, the map of orbits looks like this:
#
#         G - H       J - K - L
#        /           /
# COM - B - C - D - E - F
#                \
#                 I - SAN
#                  \
#                   YOU
# What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)



def recur(orbit):
    univ[orbit][1]+=1
    for orb in univ[orbit][0]:
        if orb in univ:
            recur(orb)

# def reverseLookup(orbit, path):


with open('input.txt') as inputFile:
    orbits = inputFile.readlines()
    print(len(orbits))
    univ = dict()
    reverseUniv = dict()
    for orbit in orbits:
        big, little = orbit[:-1].split(')')
        if little == 'YOU' or little == 'SAN':
            print(big,little)
        if big in univ:
            univ[big][0].append(little)
        else:
            univ[big] = [[little], 1]
        reverseUniv[little] = big
    total = 0
    for big, orbitlings in univ.items():
        for orb in orbitlings[0]:
            if orb in univ:
                recur(orb)
            # else:
            #     print(big)
    for k,v in univ.items():
        total += v[1]*len(v[0])
    # total += len(little)
    reversePathYOU=['524']
    reversePathSanta=['8N9'] # from line 66
    while 'COM' not in reversePathYOU:
        reversePathYOU.append(reverseUniv[reversePathYOU[-1]])
    while 'COM' not in reversePathSanta:
        reversePathSanta.append(reverseUniv[reversePathSanta[-1]])

    # startLen1 =len(reversePathYOU)
    # startLen2 = len(reversePathSanta)
    while reversePathYOU[-1] == reversePathSanta[-1]:
        reversePathYOU=reversePathYOU[:-1]
        reversePathSanta=reversePathSanta[:-1]
    # print(list(univ.keys())[list(univ.values()).index([['DLD'],1]])
    endLen1 = len(reversePathYOU)
    endLen2 = len(reversePathSanta)
    print(univ["524"], univ['8N9']) # YOU and SAN
    print(endLen1 + endLen2)
    # print(total)
