import numpy as np

images = open('input.in').read().split('\n\n')

sea_monster = [list('                  # '),list('#    ##    ##    ###'),list(' #  #  #  #  #  #   ')]

tiles = {}
for image in images:
    tile_id, pixels = image.split(':\n')
    tile_id = int(tile_id.split()[-1])
    pixels = np.array([list(p) for p in pixels.split('\n')])
    tiles[tile_id] = pixels

edges = {}

for tile, pixels in tiles.items():
    edges[tile] = {0:''.join(pixels[:,0]),1:''.join(pixels[0,:]),2:''.join(pixels[:,-1]),3:''.join(pixels[-1,:])}

matches = {tile:{i:None for i in range(4)} for tile in edges}
match_list = {tile:set() for tile in edges}

corners = []

for tile1, sides1 in edges.items():
    for tile2, sides2 in edges.items():
        if tile1 == tile2:
            continue
        else:
            for side1, binary1 in sides1.items():
                for side2, binary2 in sides2.items():
                    if binary1 == binary2:
                        matches[tile1][side1] =(tile2, side2, 'normal')
                        match_list[tile1].add(tile2)

                    elif binary1 == binary2[::-1]:
                        match_list[tile1].add(tile2)
                        matches[tile1][side1] =(tile2, side2, 'reversed')
    if sum(side is None for side in matches[tile1].values()) ==2:

        corners.append(tile1)
 
corners_prod = 1
for corner in corners:
    corners_prod *= corner
print(corners_prod)


first_corner = corners[0]
corner_order = [[first_corner]]

def opposite_side(num):
    if num == 2:
        return 0
    elif num ==0:
        return 2
    elif num == 1:
        return 3
    elif num ==3:
        return 1
    else:
        raise ValueError(f'unexpected value {num}')

def rotate_match_picture(match_number, tile, pattern_to_match, left_side=True):
    axis = 0
    if left_side == False:
        match_number = (match_number+3)%4
        axis = 1
    tiles[tile] = np.rot90(tiles[tile], k=match_number)
    if left_side:
        if pattern_to_match != ''.join(tiles[tile][:,0]):
            tiles[tile] = np.flip(tiles[tile], axis = axis)
    else:
        if pattern_to_match != ''.join(tiles[tile][0,:]):
            tiles[tile] = np.flip(tiles[tile], axis = axis)

tiles[first_corner] =np.flip(tiles[first_corner], axis = 1) #axis 1 for input.in axis 0 for example.in

l = int(len(tiles)**.5)
big_picture = np.empty((l * 8, l * 8), str)

first = True
used_tiles = set()
left_side = True

# order = []
# order2 = [[],[],[],[],[],[],[],[],[],[],[],[]]
# print(order2)

for y in range(l):
    for x in range(l):
        if not first:
            tile = next_tile
            side = next_side
            rotate_match_picture(side, tile, pattern_to_match, left_side)
        else:
            first = False
            #hardcode starting values
            tile = corners[0]
            side = 2 # 0 for example.in 2 for input.in
            big_picture[y:y+8,x:x+8] = tiles[tile][1:-1,1:-1]
            used_tiles.add(tile)
            # order.append(tile)
            # order2[y].append(tile)
            left_side = True
            pattern_to_match = ''.join(tiles[tile][:,-1])
            next_tile = matches[tile][opposite_side(side)][0]
            next_side = matches[tile][opposite_side(side)][1]
            for s,v in matches[tile].items():
                if v is None:pass
                elif v[0] not in used_tiles and next_tile != v[0]:
                    next_row_tile = v[0] 
                    next_row_side = v[1]
                    next_row_pattern = ''.join(tiles[tile][-1,:])
                    break
            continue

        big_picture[8*y:8*y+8,8*x:8*x+8] = tiles[tile][1:-1,1:-1]

        used_tiles.add(tile)
        # order.append(tile)
        # order2[y].append(tile)
        # assert(len(order) == len(used_tiles))
        if x == l-1 and y==l-1:
            break
        if x == 0:
            for s,v in matches[tile].items():
                if matches[tile][opposite_side(s)] is None:
                    if y != l-1:
                        next_tile = v[0]
                        next_side = v[1]
                    else:
                        if v[0] not in used_tiles:
                            next_tile = v[0]
                            next_side = v[1]

                elif matches[tile][opposite_side(s)][0] in used_tiles:
                    if y != l-1:
                        next_row_tile = v[0] 
                        next_row_side = v[1]
                        next_row_pattern = ''.join(tiles[tile][-1,:])
            left_side = True
            pattern_to_match = ''.join(tiles[tile][:,-1])
        elif x == l-1:
            pattern_to_match = next_row_pattern
            next_tile = next_row_tile
            next_side = next_row_side
            left_side = False
        else:
            pattern_to_match = ''.join(tiles[tile][:,-1])
            next_tile = matches[tile][opposite_side(side)][0]
            next_side = matches[tile][opposite_side(side)][1]

most_monsters=0
for _ in range(8):
    for y in range(len(big_picture) - len(sea_monster)+1):
        for x in range(len(big_picture[0]) - len(sea_monster[0])+1):
            foundMonster = True
            for j in range(len(sea_monster)):
                for i in range(len(sea_monster[0])):
                    if sea_monster[j][i] == '#':
                        if big_picture[y+j,x+i] != '#':
                            foundMonster = False
                            break

                if not foundMonster:
                    break
            else:
                if foundMonster:
                    for j in range(len(sea_monster)):
                        for i in range(len(sea_monster[0])):
                            if sea_monster[j][i] == '#':
                                big_picture[y+j,x+i] = 'O'
    big_picture = np.rot90(big_picture)
    if _ == 3:
        big_picture = np.flip(big_picture,axis=0)

print((big_picture=='#').sum())
