x = [1,1]
while True:
    x.append(x[-1] + x[-2])
    if len(str(x[-1])) >= 1000:
        break
print len(x)
