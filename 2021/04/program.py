with open('input.txt') as file:
    data = file.read().split('\n\n')

numbers = data[0].split(',')
# print(numbers)
# print(data[1])
# print()
data = [x.split() for x in data[1:]]
# print(data)

# print(data[0])
# print(data[0][1::5])
# exit()
boardsToCheck = list(range(len(data)))
print(boardsToCheck)
def checkForBingo(calledNums, boardNum, board):
    #check rows
    if any(all((x in calledNums) for x in board[y*5:y*5+5]) for y in range(5)):
        # print(board, boardNum)
        # print(calledNums)
        print(boardNum)
        boardsToCheck.remove(boardNum)
        return boardNum, calledNums, 'horizontal'
    if any(all((x in calledNums) for x in board[y::5]) for y in range(5)):
        print(boardNum)
        # print(board, boardNum)
        # print(calledNums)
        boardsToCheck.remove(boardNum)
        return boardNum, calledNums, 'vert'
    return None, None, None
for numOfNums, num in enumerate(numbers):
    for i, board in enumerate(data):
        if i in boardsToCheck:
            winningBoard, winningNumbers, winDir = checkForBingo(numbers[:numOfNums],i,board)
        if len(boardsToCheck) ==1:
            lastBoard = boardsToCheck[0]
        if len(boardsToCheck) == 0:
            break
    if len(boardsToCheck) == 0:
        break
    # if winningBoard:
    #     break

print(data[winningBoard],winDir,winningNumbers, len(winningNumbers))    
print(sum(int(x) for x in data[winningBoard] if x not in winningNumbers) * int(winningNumbers[-1]))

