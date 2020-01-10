# --- Part Two ---
# All this drifting around in space makes you wonder about the nature of the universe. Does history really repeat itself? You're curious whether the moons will ever return to a previous state.
#
# Determine the number of steps that must occur before all of the moons' positions and velocities exactly match a previous point in time.
#
# For example, the first example above takes 2772 steps before they exactly match a previous point in time; it eventually returns to the initial state:
#
# After 0 steps:
# pos=<x= -1, y=  0, z=  2>, vel=<x=  0, y=  0, z=  0>
# pos=<x=  2, y=-10, z= -7>, vel=<x=  0, y=  0, z=  0>
# pos=<x=  4, y= -8, z=  8>, vel=<x=  0, y=  0, z=  0>
# pos=<x=  3, y=  5, z= -1>, vel=<x=  0, y=  0, z=  0>
#
# After 2770 steps:
# pos=<x=  2, y= -1, z=  1>, vel=<x= -3, y=  2, z=  2>
# pos=<x=  3, y= -7, z= -4>, vel=<x=  2, y= -5, z= -6>
# pos=<x=  1, y= -7, z=  5>, vel=<x=  0, y= -3, z=  6>
# pos=<x=  2, y=  2, z=  0>, vel=<x=  1, y=  6, z= -2>
#
# After 2771 steps:
# pos=<x= -1, y=  0, z=  2>, vel=<x= -3, y=  1, z=  1>
# pos=<x=  2, y=-10, z= -7>, vel=<x= -1, y= -3, z= -3>
# pos=<x=  4, y= -8, z=  8>, vel=<x=  3, y= -1, z=  3>
# pos=<x=  3, y=  5, z= -1>, vel=<x=  1, y=  3, z= -1>
#
# After 2772 steps:
# pos=<x= -1, y=  0, z=  2>, vel=<x=  0, y=  0, z=  0>
# pos=<x=  2, y=-10, z= -7>, vel=<x=  0, y=  0, z=  0>
# pos=<x=  4, y= -8, z=  8>, vel=<x=  0, y=  0, z=  0>
# pos=<x=  3, y=  5, z= -1>, vel=<x=  0, y=  0, z=  0>
# Of course, the universe might last for a very long time before repeating. Here's a copy of the second example from above:
#
# <x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>
# This set of initial positions takes 4686774924 steps before it repeats a previous state! Clearly, you might need to find a more efficient way to simulate the universe.
#
# How many steps does it take to reach the first state that exactly matches a previous state?

class Planet():
    def __init__(self,x,y,z,name):
        self.x = x
        self.y = y
        self.z = z
        self.i = 0
        self.j = 0
        self.k = 0
        self.ai = 0
        self.aj = 0
        self.ak = 0
        self.name = name

    def __str__(self):
        return f'Planet {self.name} pos:x={self.x}, y={self.y}, z={self.z} vel:i={self.i}, j={self.j}, k={self.k}'

    def get_pos(self):
        return (self.x, self.y, self.z)

    def get_vel(self):
        return (self.i, self.j, self.k)

    def get_accel(self):
        return (self.ai, self.aj, self.ak)

    def reset_accel(self):
        self.ai = 0
        self.aj = 0
        self.ak = 0

    def calc_accel(self, other):
        if self.x < other.x:
            self.ai += 1
        elif self.x > other.x:
            self.ai -=1
        if self.y < other.y:
            self.aj += 1
        elif self.y > other.y:
            self.aj -=1
        if self.z < other.z:
            self.ak += 1
        elif self.z > other.z:
            self.ak -=1

    def update_velocity(self):
        self.i += self.ai
        self.j += self.aj
        self.k += self.ak

    def update_position(self):
        self.x += self.i
        self.y += self.j
        self.z += self.k

    def get_potential(self):
        return abs(self.x)+abs(self.y)+abs(self.z)

    def get_kinetic(self):
        return abs(self.i)+abs(self.j)+abs(self.k)

    def get_total_energy(self):
        return self.get_potential() * self.get_kinetic()

    def __eq__(self, other):
        return (self.x == other.x and
                self.y == other.y and
                self.z == other.z and
                self.i == other.i and
                self.j == other.j and
                self.k == other.k)

    def __ne__(self,other):
        return not self.__eq__(other)

def cycle(planets):
    for i in range(len(planets)):
        planets[i].reset_accel()
        for pl in planets[:i]:
            planets[i].calc_accel(pl)
        try:
            for pl in planets[i+1:]:
                planets[i].calc_accel(pl)
        except IndexError as e:
            print(e)

    for planet in planets:
        planet.update_velocity()
        planet.update_position()

    return planets

planets=[]
planets.append(Planet(x=-2,y=9,z=-5,name='Io'))
planets.append(Planet(x=16,y=19,z=9,name='Europa'))
planets.append(Planet(x=0,y=3,z=6,name='Callisto')) #y=3
planets.append(Planet(x=11,y=0,z=11,name='Ganymede'))
Io = Planet(x=-2,y=9,z=-5,name='Io')
Europa = Planet(x=16,y=19,z=9,name='Europa')
Callisto = Planet(x=0,y=3,z=6,name='Callisto')
Ganymede = Planet(x=11,y=0,z=11,name='Ganymede')
original_state=[Io,Europa,Callisto,Ganymede]
x_axis = [planets[0].x, planets[1].x, planets[2].x, planets[3].x, planets[0].i, planets[1].i, planets[2].i, planets[3].i]
y_axis = [planets[0].y, planets[1].y, planets[2].y, planets[3].y, planets[0].j, planets[1].j, planets[2].j, planets[3].j]
z_axis = [planets[0].z, planets[1].z, planets[2].z, planets[3].z, planets[0].k, planets[1].k, planets[2].k, planets[3].k]
cycle(planets)
print(x_axis,y_axis,z_axis)
# exit()
i =1
# while (
#        planets[0]!=Io and
#        planets[1]!=Europa and
#        planets[2]!=Callisto and
#        planets[3]!=Ganymede
#        ):
#     cycle(planets)
#     i+=1
#     if i > 1000000:
#         break
#     # if i %100 == 0:
#     #     print(i)
#     if [planets[0].x, planets[1].x, planets[2].x, planets[3].x, planets[0].i, planets[1].i, planets[2].i, planets[3].i] == x_axis:
#         print(i,'x')
#     if [planets[0].y, planets[1].y, planets[2].y, planets[3].y, planets[0].j, planets[1].j, planets[2].j, planets[3].j] == y_axis:
#         print(i, 'y')
#     if [planets[0].z, planets[1].z, planets[2].z, planets[3].z, planets[0].k, planets[1].k, planets[2].k, planets[3].k] == z_axis:
#         print(i,'z')
    # for pl in range(len(planets)):
    #     if planets[pl].x==original_state[pl].x and planets[pl].i==original_state[pl].i:
    #         print(planets[pl].name, i)
    # print(planets[0].y,planets[0].j)
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

# Function to return LCM of two numbers
def lcm(a,b):
    return (a*b) / gcd(a,b)
x_cycle = 186028
y_cycle = 286332
z_cycle = 96236
print(i,*planets)
print(lcm(lcm(x_cycle,y_cycle),z_cycle))

# Io Ganymede
# -2, 11 = 16           -13
# 9, 0 = 12              9
# -5, 11 = 16            -16

# Io Europa
# -2, 16 = 16             -18
# 9, 19 = 12            -10
# -5, 9 = 16              -16

# Io Callisto
# -2, 0 = 6              -2
# 9, 3 = 10               6
# -5, 6 = 12             -11

# Europa Callisto
# 16, 0 = 16               16
# 19, 3 = 16               16
# 9, 6 = 8                 3

# Europa Ganymede
# 16, 11 = 8              5
# 19, 0 = 16              19
# 9, 11 = 6               -2

#Callisto Ganymede
# 0, 11 = 12             -11
# 3, 0 = 8                3
# 6, 11 = 8               -5


# fplanets=[]
# fplanets.append(Planet(x=0,y=-1,z=1,name='Io'))
# fplanets.append(Planet(x=0,y=0,z=1,name='Europa'))
# fplanets.append(Planet(x=0,y=1,z=1,name='Callisto')) #y=3
# fplanets.append(Planet(x=11,y=0,z=11,name='Ganymede'))
# Io = Planet(x=0,y=-1,z=1,name='Io')
# Europa = Planet(x=0,y=0,z=1,name='Europa')
# Callisto = Planet(x=0,y=1,z=1,name='Callisto')
# Ganymede = Planet(x=0,y=0,z=0,name='Ganymede')
# foriginal_state=[Io,Europa,Callisto,Ganymede]
# cycle(fplanets)
# i =1
# while (
#        fplanets[0]!=Io and
#        fplanets[1]!=Europa and
#        fplanets[2]!=Callisto
#        # fplanets[3]!=Ganymede
#        ):
#     cycle(fplanets)
#     i+=1
#     if i > 1000000:
#         break
#     # if i %100 == 0:
#     #     print(i)
#     # for pl in range(len(fplanets)):
#     #     if fplanets[pl].x==foriginal_state[pl].x and fplanets[pl].i==foriginal_state[pl].i:
#     #         print(fplanets[pl].name, i)
#     print(fplanets[0].x,fplanets[0].i)
# print(i,*fplanets)
