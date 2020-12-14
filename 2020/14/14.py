from itertools import zip_longest

with open('input.in') as file:
    program = file.read()[7:].split('\nmask = ')

def apply_mask(mask, num):
    bin_num=''
    for i,j in zip_longest(mask,bin(num)[2:].zfill(36),fillvalue='0'):
        if i == 'X':
            bin_num += j
        else:
            bin_num += i
    return int(bin_num,2)

addresses = defaultdict()
for i in program:
    split = i.split('\nmem[')
    mask = split[0]
    for line in split[1:]:
        addr, val = list(map(int,line.split('] = ')))
        addresses[addr]=apply_mask(mask,val)
print(sum(addresses.values()))

# part 2

def apply_addr_mask(addr, mask):
    return_addresses = ['']
    for i,j in zip_longest(mask,bin(addr)[2:].zfill(36),fillvalue='0'):
        if i == '1':
            for a in range(len(return_addresses)):
                return_addresses[a] +='1'
        elif i == '0':
            for a in range(len(return_addresses)):
                return_addresses[a] += j
        else:
            return_addresses *=2
            l = len(return_addresses)
            for a in range(l):
                if a<l/2:
                    return_addresses[a] +='0'
                else:
                    return_addresses[a] +='1'
    return return_addresses

addresses = {}
for i in program:
    split = i.split('\nmem[')
    mask = split[0]
    for line in split[1:]:
        addr, val = list(map(int,line.split('] = ')))
        # print(addr)
        for i in apply_addr_mask(addr, mask):
            addresses[int(i,2)]=val
print(sum(addresses.values()))