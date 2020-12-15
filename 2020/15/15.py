input_ = [5,1,9,18,13,8,0]
e1 = [0,3,6]
e2 = [1,3,2]
e3 = [2,1,3]
e4 = [1,2,3]
e5 = [2,3,1]
e6 = [3,2,1]
e7 = [3,1,2]
# input_ = e1

last_indices = {i:input_.index(i) for i in input_}

last = input_[-1]
last_indices[last] = 0

for i in range(len(input_)-1, 30_000_000-1):
    if last_indices[last] != 0:
        spoken = last_indices[last]
        last_indices[last] = i
    else:
        spoken = 0
        last_indices[last] = i
    if spoken in last_indices.keys():
        last_indices[spoken] = i - last_indices[spoken] +1
    else:
        last_indices[spoken] = 0
    last = spoken
    if i == 2018: #good ol' off-by-two
        print(last)
print(last)
