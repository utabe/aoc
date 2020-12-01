output = []
d = 0
ballx = 0
base = 0
score = 0
paddlex = 0

def intcode():
    global base, d
    inp = open('input.txt').read().split(',')
    lst = list(map(int, inp))
    lst[0] = 2 #Modifying input according to task
    [lst.append(0) for rin in range(10000)]

    def one(second, third, fourth):
        nonlocal lst
        lst[fourth] = lst[second] + lst[third]

    def two(second, third, fourth):
        nonlocal lst
        lst[fourth] = lst[second] * lst[third]

    def three(second, third, fourth):
        global paddlex, ballx
        nonlocal lst
        if ballx > paddlex: change = 1
        elif ballx < paddlex: change = -1
        else: change = 0
        lst[second] = change

    def four(second, third, fourth):
        nonlocal lst
        global output, ballx, paddlex, score
        output.append(lst[second])
        if len(output) % 3 == 0:
            if lst[second] == 4:
                ballx = output[-3]
            if lst[second] == 3:
                paddlex = output[-3]
            if output[-3] == -1 and output[-2] == 0:
                score = output[-1]


    def five(second, third, fourth):
        nonlocal lst
        global d
        if lst[second] != 0:
            d = lst[third] - 4
        else:
            d -= 1

    def six(second, third, fourth):
        nonlocal lst
        global d
        if lst[second] == 0:
            d = lst[third] - 4
        else:
            d -= 1

    def seven(second, third, fourth):
        nonlocal lst
        if lst[second] < lst[third]:
            lst[fourth] = 1
        else:
            lst[fourth] = 0

    def eight(second, third, fourth):
        nonlocal lst
        if lst[second] == lst[third]:
            lst[fourth] = 1
        else:
            lst[fourth] = 0

    def nine(second, third, fourth):
        nonlocal lst
        global base
        base += lst[second]

    def ninetynine(second, third, fourth):
        print(score)
        quit()

    command = {1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine, 99: ninetynine}

    while 1:
        beg = str(lst[d])
        opcode = int(beg[-2:])

        try:
            second = int(beg[-3])
        except:
            second = 0
        try:
            third = int(beg[-4])
        except:
            third = 0
        try:
            fourth = int(beg[-5])
        except:
            fourth = 0

        e = (d+1)
        f = (d+2)
        g = (d+3)
        if second != 1:
            e = lst[e]
            if second == 2:
                e = e+base
        if third !=1:
            f = lst[f]
            if third == 2:
                f = f+base
        if fourth != 1:
            g = lst[g]
            if fourth == 2:
                g = g+base
        command[opcode](e,f,g)
        if opcode == 4 or opcode == 3 or opcode == 9:
            d += 2
        elif opcode == 99:
            return
        else:
            d += 4

intcode()
