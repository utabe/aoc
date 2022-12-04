with open('input.txt') as file:
    connections = [x.split('-') for x in file.read().split()]

conns = {'start':[]}
for con in connections:
    if 'start' in con:
        if con[0]=='start':
            conns['start'].append(con[1])
        else:
            conns['start'].append(con[0])
    else:
        if con[0] in conns:
            conns[con[0]].append(con[1])
        else:
            conns[con[0]] = [con[1]]
        if con[1] in conns:
            conns[con[1]].append(con[0])
        else:
            conns[con[1]] = [con[0]]
            
print(connections)
print(conns)
paths = [(['start'],False)]
while any(path[0][-1]!='end' for path in paths):
    for path in paths[:]:
        if path[0][-1]=='end':
            continue
        # print(path[0][-1],'heyo')
        # print(paths)
        for p in conns[path[0][-1]]:
            # if p.lower() == p and p in path:
            if p.lower() == p and p in path[0] and path[1]==True:
                continue
            if p.lower() == p and path[0].count(p) ==1:
                paths.append((path[0]+[p],True))
            else:
                paths.append((path[0]+[p],path[-1]))
            # if p.lower() == p and path[0].count(p) >=2:
                # path[1]=True
                # path = (path[0],True)
        paths.remove(path)
# print(paths)
print(len(paths))