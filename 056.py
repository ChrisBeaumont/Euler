from util import digits

answer = 0
for a in range(100):
    for b in range(100):
        answer = max(answer, sum(digits(a**b)))

print answer
