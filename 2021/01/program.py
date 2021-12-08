with open('input.txt', 'r') as file:
    slopes = list(map(int,file.read().split('\n')))

counter =0
current_amount = slopes[0]

for i in slopes:
    if i > current_amount:
        counter+=1
    current_amount=i
print(counter)

counter2 = 0
current_window_ammount = sum(slopes[0:3])

for i, v in enumerate(slopes[0:-2]):
    window_ammount = sum(slopes[i:i+3])
    # print(window_ammount, current_window_ammount)
    if window_ammount > current_window_ammount:
        counter2 +=1
        # if counter > 3: exit()
    current_window_ammount = window_ammount
print(counter2)