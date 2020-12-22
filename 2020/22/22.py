# from collections import deque

deck1, deck2 = open('input.in').read().split('\n\n')
# deck1 = deque(map(int,deck1.split('\n')[1:]))
# deck2 = deque(map(int,deck2.split('\n')[1:]))
deck1 = list(map(int,deck1.split('\n')[1:]))
deck2 = list(map(int,deck2.split('\n')[1:]))

# part 1
# while deck1 and deck2:
#     d1 = deck1.popleft()
#     d2 = deck2.popleft()

#     if d1 > d2:
#         deck1.append(d1)
#         deck1.append(d2)
#     else:
#         deck2.append(d2)
#         deck2.append(d1)
# total = 0
# for i, num in enumerate(reversed(deck2)):
#     total += (i+1) * num
# print(total)

count = 0
def play_game(deck1,deck2):
    prev_games = set()

    while deck1 and deck2:
        if str(deck1) + ' ' + str(deck2) in prev_games:
            winner = 'd1'
            return winner,deck1,deck2
        else: 
            prev_games.add(str(deck1) + ' ' + str(deck2))
        # d1 = deck1.popleft()
        # d2 = deck2.popleft()

        d1 = deck1[0]
        deck1 = deck1[1:]
        d2 = deck2[0]
        deck2 = deck2[1:]
        
        if len(deck1) >= d1 and len(deck2) >= d2:
            #recursive combat!
            winner,*_ = play_game(deck1[:d1], deck2[:d2])
            if winner == 'd1':
                deck1.append(d1)
                deck1.append(d2)
            else:
                deck2.append(d2)
                deck2.append(d1)
        elif d1 > d2:
            deck1.append(d1)
            deck1.append(d2)
        else:
            deck2.append(d2)
            deck2.append(d1)

    if deck1:
        winner = 'd1'
    else:
        winner = 'd2'

    return winner, deck1, deck2


winner,deck1,deck2 = play_game(deck1,deck2)
if winner == 'd1':
    win_deck = deck1
else:
    win_deck = deck2
total = 0
for i, num in enumerate(reversed(win_deck)):
    total += (i+1) * num

print(total)