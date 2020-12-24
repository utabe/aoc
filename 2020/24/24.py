paths = [list(line) for line in open('input.in').read().split('\n')]

tiles={}

mapping = {'e': 1, 'w': -1, 'ne': 1+1j, 'sw': -1-1j, 'nw': 1j, 'se': -1j}

for path in paths:
    tile = 0 + 0j
    while path:
        if path[0] == 'e' or path[0]=='w':
            direction = path[0]
            path = path[1:]
        else:
            direction = path[:2]
            path = path[2:]

        tile += mapping[''.join(direction)]
    if tile in tiles:
        tiles[tile] += 1
    else:
        tiles[tile] = 1
    
# part1
print(sum(t%2 for t in tiles.values()))

def get_neighbors(tile):
    return [value + tile for value in mapping.values()]

def day_passes(tiles):
    tiles_2 = tiles.copy()

    for tile in tiles.keys():
        for neighbor in get_neighbors(tile):
            if neighbor not in tiles_2:
                tiles_2[neighbor] = 0
    
    for tile, state in tiles_2.items():
        number_of_live_neighboors = sum(tiles[neighbor]%2 for neighbor in get_neighbors(tile) if neighbor in tiles)

        if state%2:
            if number_of_live_neighboors == 0 or number_of_live_neighboors > 2:
                tiles_2[tile]+=1
        else:
            if number_of_live_neighboors == 2:
                tiles_2[tile]+=1

    return tiles_2

for day in range(100):
    tiles = day_passes(tiles)

print(sum(t%2 for t in tiles.values()))