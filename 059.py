from itertools import product
from util import dictionary

words = dictionary()
code = map(int, open('cipher1.txt').read().split(','))

best_score = 0
best_msg = ''
best_password = None
answer = None

#ascii values of a-z
lowercase = range(ord('a'), ord('z') + 1)
for key in product(lowercase, repeat=3):
    msg_ascii = [code[i] ^ key[i % 3] for i in range(len(code))]
    msg_txt = ''.join(map(chr, msg_ascii))
    #look at first 50 words to test for match
    score = sum((s in words for s in msg_txt.split()[0:50]))
    if score > best_score:
        best_score = score
        best_msg = msg_txt
        best_password = key
        answer = sum(msg_ascii)
        if score > 10: break

print answer
#print best_msg, best_password
