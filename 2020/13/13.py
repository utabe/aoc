from math import prod

with open('input.in') as file:
    departure = int(file.readline().strip())
    routes = file.readline().strip()
    bus_times = list(map(int,routes.replace(',x','').split(',')))

routes = routes.split(',')
tuples = [(int(val), idx) for idx, val in enumerate(routes) if val !='x']

X = 0
l = 0
jumpby = 1
while not all((X+i)%val==0 for val,i in tuples):
    if all((X+i)%val==0 for val,i in tuples[:l]):
        jumpby = prod(t[0] for t in tuples[:l])
        l +=1
    X += jumpby

print(X)

# part 1
min_id = min(bus_times,key=lambda x:x- (departure%x))
print(min_id * (min_id - (departure%min_id)))

