with open('example.txt') as file:
    numbers = file.read().split()

print(numbers)

class SnailNumber():
    def __init__(self, startList):
        if isInstance(startList[0], int):
            self.x = 