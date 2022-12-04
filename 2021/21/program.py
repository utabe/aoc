ex1 = 4
ex2 = 8
input1 = 6
input2 = 10

ex1 = input1
ex2 = input2

turns = 1
die = 1
points1 = 0
points2 = 0
dieRolls = 0
def tripleDie(playerLoc, playerPoints, die):
    move = 0
    for _ in range(3):
        move += die
        die += 1
        if die == 101:
            die = 1
    global dieRolls
    dieRolls += 3
    playerLoc += move
    while playerLoc > 10:
        playerLoc -=10
    playerPoints += playerLoc
    # if playerPoints >=1000:
    #     break
    return playerLoc, playerPoints, die
    
while points1 < 1000 and points2 < 1000:
    ex1, points1, die = tripleDie(ex1,points1, die)
    turns +=1
    if points1 >=1000:
        break
    ex2, points2, die = tripleDie(ex2,points2, die)
    turns +=1
    # print("points1:",points1,"points2",points2,turns)
    
print(points1, points2, turns, dieRolls)