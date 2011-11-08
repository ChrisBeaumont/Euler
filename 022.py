names = open('names.txt').read().split(',')
names = sorted([n.strip()[1:-1] for n in names])
offset = ord('A')
scores = [sum(map(lambda x:ord(x) - offset + 1, n)) for n in names]
score = sum((s * (i+1) for i,s in enumerate(scores)))

print score
