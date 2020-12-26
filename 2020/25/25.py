card_pub = 9_093_927
door_pub = 11_001_876

example_card = 5_764_801
example_door = 17_807_724

card_start_value = 1

subject = 7

divval = 20201227

# def loop(value):
#     value = value * 7
#     value = value % divval

#     print(value)
# import pdb; pdb.set_trace()
# for loop_size in range(1,2000000):


#Get the loop values
value = 1
for i in range(20000000):
    
    value = value * subject
    
    # print('val','divval',value, value % divval)
    value = value % divval
    if value == card_pub or value == door_pub:
        print('true',value, i)
    if value == example_card or value == example_door:
        print('example',value, i)
    
#loop numbers
card_loop = 4535883 +1
door_loop = 14984026 +1

sub = door_pub
val = 1
for loop in range(card_loop):
    val = val * sub
    val = val % divval
print(val)

sub2 = card_pub
val2 = 1
for loop in range(door_loop):
    val2 = val2 * sub2
    val2 = val2 % divval
print(val2)