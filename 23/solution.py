import intcode
from collections import deque
from itertools import count

with open('input.in') as file:
    input = file.read()


def init():
    prog = intcode.parse(input)
    qs = [deque() for i in range(50)]
    procs = []
    for i in range(50):
        proc = intcode.run(prog.copy())
        procs.append(proc)
        next(proc)
        v = proc.send(i)
        assert v == None
    return procs, qs

def runnet(procs, qs):
    for step in count():
        for i,q in enumerate(qs):
            p = procs[i] # it is in input state
            if len(q)>0:
                assert len(q)>=2
                v = p.send(q.popleft())
                assert v==None
                v = p.send(q.popleft())
            else:
                v = p.send(-1)
            while v != None:
                addr = v
                x = next(p)
                y = next(p)
                v = next(p)
                if addr == 255:
                    return x,y
                qs[addr].append(x)
                qs[addr].append(y)

procs, qs = init()
print(runnet(procs, qs))



def runnet2(procs, qs):
    nat = (0,0)
    lastnat = nat
    for step in count():
        for i,q in enumerate(qs):
            p = procs[i] # it is in input state
            if len(q)>0:
                assert len(q)>=2
                v = p.send(q.popleft())
                assert v==None
                v = p.send(q.popleft())
            else:
                v = p.send(-1)
            while v != None:
                addr = v
                x = next(p)
                y = next(p)
                v = next(p)
                if addr == 255:
                    nat = x,y
                    continue
                qs[addr].append(x)
                qs[addr].append(y)

        if sum(map(len,qs))>0:
            continue

        if nat[1] == lastnat[1]:
            return nat[1]
        lastnat = nat
        qs[0].append(nat[0])
        qs[0].append(nat[1])



procs, qs = init()
print(runnet2(procs, qs))
