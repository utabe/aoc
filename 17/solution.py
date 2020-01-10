no_write = [4, 5, 6, 9]
no_inc = [5, 6]
values = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}
memory = 5000
hx = (1, -1, 0, 0)
hy = (0, 0, 1, -1)
moves = "RLDU"
moves_in = "LRUD"
headings = [90, 270, 0, 180]
corn_moves = ["LU", "LD", "RU", "RD"]
f_names = "ABC"

def op1(): # Add two values and stores it
    a[write] = read[0] + read[1]

def op2(): # Multiply two values and stores it
    a[write] = read[0] * read[1]

def op3(): # Stores value
    global w
    a[write] = inps[w]
    w += 1

def op4(): # Outputs value
    outs.append(read[0])

def op5(): # If value 1 is non-zero, changes pointer to second value
    global j, c
    if read[0] != 0:
        c = read[1]
        j = True

def op6(): # If value 1 is zero, changes pointer to second value
    global j, c
    if read[0] == 0:
        c = read[1]
        j = True

def op7(): # If value 1 is less than value 2, 1 is stored, else 0 is stored
    if read[0] < read[1]: a[write] = 1
    else: a[write] = 0

def op8(): # If value 1 is equal to value 2, 1 is stored, else 0 is stored
    if read[0] == read[1]: a[write] = 1
    else: a[write] = 0

def op9(): # Increases relative base
    global rb
    rb += read[0]

def mr(x, y): # x is params, y is modes
    global rb
    v = []
    for i in range(len(x)):
        if y[i] == 0:
            v.append(a[x[i]])
        elif y[i] == 1:
            v.append(x[i])
        else:
            v.append(a[x[i] + rb])
    return v

def mw(x, y): # x is param, y is mode
    global rb
    if y == 0: return x
    else: return x + rb

def run():
    global c, j, read, write
    j = False # Check if jumped (case 5, 6)
    p = a[c] # Current value
    o = p % 100 # Operation code
    n = values[o] # Value to increase
    p //= 100
    m = [] # Modes
    for i in range(n - 1):
        m.append(p % 10)
        p //= 10
    read = a[c + 1:c + n - 1] # Current read params
    if o in no_write: # Add last parameter if special case
        k = 0
        read.append(a[c + n - 1])
    else: # Remove last mode if not special case
        k = m[-1]
        m = m[:-1]
    read = mr(read, m) # Values after converting modes
    write = mw(a[c + n - 1], k) # Write params
    exec("op%d()" % o) # Execute operation code
    if not j: # Increase pointer if not jumped (case 5, 6)
        c += n

def program(t, x): # t is program, x is inputs
    global a, c, f, outs, inps, w, rb
    outs = []
    inps = x[:]
    a = t[:]
    a += [0] * (memory - len(a))
    w = 0
    c = 0
    rb = 0
    while True:
        run()
        if a[c] == 99: # Halt if current value is 99
            break
    return outs

def camera_feed(): # For debugging purposes
    print("\n".join(["".join(x) for x in matrix]))

def check_path(x, y):
    a = list(x)
    b = list(y)
    if a[1] == b[1]:
        py = a[1]
        m = a[0]
        n = b[0]
        if m > n:
            d = 0
            m, n = n, m
        else:
            d = 180
        for i in range(m + 1, n):
            if matrix[i][py] == ".":
                return None
        return (moves[headings.index((d - h) % 360)], n - m)
    if a[0] == b[0]:
        px = a[0]
        m = a[1]
        n = b[1]
        if m > n:
            d = 270
            m, n = n, m
        else:
            d = 90
        for i in range(m + 1, n):
            if matrix[px][i] == ".":
                return None
        return (moves[headings.index((d - h) % 360)], n - m)
    return None

def find_path():
    global h
    corns_pos = list(corns.keys())
    order = [(rx, ry)]
    path = []
    h = 0
    while len(corns_pos) > 0:
        for x in corns_pos:
            k = check_path(order[-1], x)
            if k:
                h += headings[moves.index(k[0])]
                h %= 360
                order.append(x)
                path.append(k)
                corns_pos.remove(x)
                break
    px, py = order[-1]
    d = moves[headings.index((headings[moves.index(path[-1][0])] + h) % 360)]
    fd = list(corns[order[-1]])
    fd.remove(moves[moves_in.index(d)])
    fd = fd[0]
    dx = hx[moves.index(fd)]
    dy = hy[moves.index(fd)]
    s = 0
    while True:
        px += dx
        py += dy
        if not (0 <= px < height and 0 <= py < width) or (matrix[px][py] == "."):
            break
        s += 1
    path.append((moves[headings.index((headings[moves.index(d)] - h) % 360)], s))
    return path

def create_key(path):
    key = {}
    i = 0
    s = ""
    for x in path:
        if x not in key.values():
            key[chr(i + 97)] = x
            i += 1
        for m in key.keys():
            if key[m] == x:
                s += m
    return (key, s)

def compress(s, x): # Use backtracking to compress string
    global f
    if len(s) == 0:
        f = x
        return
    for i in range(1, 6):
        t = s[:i]
        if t in x:
            compress(s[i:], x)
        elif len(x) < 3:
            compress(s[i:], x + [t])

def part1():
    global matrix, rx, ry, corns, width, height
    a = t[:]
    values = program(a, [])
    matrix = [[]]
    for x in values:
        c = chr(x)
        if c == "\n":
            matrix.append([])
        else:
            matrix[-1].append(c)
            if c in "^>v<":
                rx = len(matrix) - 1
                ry = len(matrix[-1]) - 1
    matrix = matrix[:-2]
    height = len(matrix)
    width = len(matrix[0])
    s = 0
    corns = {}
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == "#":
                n = 0
                d = ""
                for k in range(4):
                    px = i + hx[k]
                    py = j + hy[k]
                    if 0 <= px < height and 0 <= py < width and matrix[px][py] == "#":
                        n += 1
                        d += moves[k]
                if n == 4:
                    matrix[i][j] = "O"
                    s += i * j
                if d in corn_moves:
                    corns[(i, j)] = d
                    matrix[i][j] = "X"
    print(s)

def part2():
    path = find_path()
    key, s = create_key(path)
    compress(s, [])
    functions = []
    for i in range(3):
        p = []
        for x in f[i]:
            p += list(map(str, key[x]))
        functions.append(",".join(p) + "\n")
        s = s.replace(f[i], f_names[i])
    routine = [",".join(list(s)) + "\n"]
    feed = ["n" + "\n"]
    values = []
    for x in routine + functions + feed:
        values += list(map(ord, x))
    a = t[:]
    a[0] = 2
    print(program(a, values)[-1])

t = list(map(int, open("input.in").read().split(",")))

part1() # Part 1
part2() # Part 2
