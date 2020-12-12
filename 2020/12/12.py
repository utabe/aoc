directions = [(line[0], int(line[1:])) for line in open('input.in').read().split('\n')]

state = [0+0j, 90]
compass = dict(N=1j,S=-1j,E=1,W=-1)
facing = {0:'N',90:'E',180:'S',270:'W'}
for d, v in directions:
    if d in compass:
        state[0] += compass[d] * v
    elif d == 'F':
        state[0] += compass[facing[state[1]]] * v
    elif d in 'RL':
        state[1] = (state[1] + v * [1,-1][d=='L'])%360 
    else:
        raise ValueError('Unexpected Direction', d)
print(state)
print(abs(state[0].real)+abs(state[0].imag))

# Part 2
ship = 0+0j
waypoint = 10+1j
for d, v in directions:
    if d in compass:
        waypoint += compass[d] * v
    elif d == 'F':
        ship += waypoint * v
    elif d in 'RL':
        for i in range(int(v/90)):
            waypoint *= (1j *[-1,1][d=='L'])
print(waypoint, ship)
print(abs(ship.real)+abs(ship.imag))




# print(facing)