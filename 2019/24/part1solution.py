grid = 0
with open("input.in") as f:
    i = 0
    for line in f:
        for c in line.strip():
            if c == "#":
                grid += 1 << i
            i += 1

seen = set()
while grid not in seen:
    seen.add(grid)

    new_grid = 0
    for i in range(25):
        count = 0
        if i >= 5:
            count += (grid >> (i - 5)) & 1

        if i < 20:
            count += (grid >> (i + 5)) & 1

        if i % 5:
            count += (grid >> (i - 1)) & 1

        if i % 5 != 4:
            count += (grid >> (i + 1)) & 1

        if count == 1 or (count == 2 and not ((grid >> i) & 1)):
            new_grid |= 1 << i
    grid = new_grid

print(grid)
