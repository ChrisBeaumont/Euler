num = 380 # smallest factor of 10, 19, and 20
while(True):
    isdiv = True
    for i in range(1, 21):
        if num % i != 0: 
            isdiv = False
            break
    if isdiv:
        break
    num += 380

print num
