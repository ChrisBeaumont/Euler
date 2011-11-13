answer = 0
for i in range(10000):
    num = str(i)
    answer += 1
    for j in range(50):
        num = str(int(num) + int(num[::-1]))
        if num == num[::-1]:
            #print i, j, num
            answer -= 1
            break
print answer
