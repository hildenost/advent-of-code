door_key = 17807724
card_key = 5764801

door_key = 18499292 
card_key = 8790390 

VALUE = 20201227

# Only ONE loop_size is needed to find the answer, but
# here are both
value = 1
door_loop_size = 0
subject_n = 7
while door_key != value:
    door_loop_size += 1
    value *= subject_n
    value %= VALUE

value = 1
card_loop_size = 0
while card_key != value:
    card_loop_size += 1
    value *= subject_n
    value %= VALUE

encryption = 1
for i in range(door_loop_size):
    encryption *= card_key
    encryption %= VALUE
print(encryption)
encryption = 1
for i in range(card_loop_size):
    encryption *= door_key
    encryption %= VALUE
print(encryption)
