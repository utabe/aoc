grid = 0
with open("input.in") as f:
    i = 0
    for line in f:
        for c in line.strip():
            if c == "#":
                grid += 1 << i
            i += 1

levels = [0, 0, grid, 0, 0]
for _ in range(200):
    new_levels = [0, 0]

    for j, grid in enumerate(levels[1:-1]):
        new_grid = 0

        for i in range(25):
            if i == 12:
                continue

            count = 0

            if i == 17:
                prev = levels[j + 2] >> 20
                while prev:
                    count += prev & 1
                    prev >>= 1
            elif i >= 5:
                count += (grid >> (i - 5)) & 1
            else:
                count += (levels[j] >> 7) & 1

            if i == 7:
                prev = levels[j + 2] & 31
                while prev:
                    count += prev & 1
                    prev >>= 1
            elif i < 20:
                count += (grid >> (i + 5)) & 1
            else:
                count += (levels[j] >> 17) & 1

            if i == 13:
                for k in range(4, 25, 5):
                    count += (levels[j + 2] >> k) & 1
            elif i % 5:
                count += (grid >> (i - 1)) & 1
            else:
                count += (levels[j] >> 11) & 1

            if i == 11:
                for k in range(0, 25, 5):
                    count += (levels[j + 2] >> k) & 1
            elif i % 5 != 4:
                count += (grid >> (i + 1)) & 1
            else:
                count += (levels[j] >> 13) & 1

            if count == 1 or (count == 2 and not ((grid >> i) & 1)):
                new_grid |= 1 << i

        new_levels.append(new_grid)

    new_levels.extend([0, 0])
    levels = new_levels

res = 0
for grid in levels:
    while grid:
        res += grid & 1
        grid >>= 1

print(res)
