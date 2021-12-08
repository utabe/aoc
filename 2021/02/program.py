x = 0
y = 0

with open('input.txt','r') as f:
    for line in f.readlines():
        command, i = line.split()
        if command == "forward":
            x += int(i)
        elif command == "down":
            y += int(i)
        else:
            y -= int(i)

print(x,y,x*y)

#part2
x=0
y=0
aim=0

with open('input.txt','r') as f:
    for line in f.readlines():
        command, i = line.split()
        if command == "forward":
            x += int(i)
            y+= aim * int(i)
        elif command == "down":
            aim += int(i)
        else:
            aim -= int(i)

print(x,y,x*y)