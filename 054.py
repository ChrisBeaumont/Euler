"""
The file, poker.txt, contains one-thousand random hands dealt to two
players. Each line of the file contains ten cards (separated by a
single space): the first five are Player 1's cards and the last five
are Player 2's cards. You can assume that all hands are valid (no
invalid characters or repeated cards), each player's hand is in no
specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?


Just lots of logic here. Nothing fancy. 

But see http://www.suffecool.net/poker/evaluator.html for a nice, fast
method
"""
key = dict(zip( ('2','3','4','5','6','7','8','9','T', 'J', 'Q', 'K', 'A'),
                (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)))

def sort(hand):
    hand = sorted(hand, key=lambda x: key[x[0]])
    ranks = [key[h[0]] for h in hand]
    suits = [h[1] for h in hand]
    return ranks, suits

def kicker(r1, r2):
    for i in range(4, -1, -1):
        if r1[i] == r2[i]: continue
        result = 1 if r1[i] > r2[i] else 2
        return result
    return 0

def pair(ranks, suits):
    p = None
    for i in range(4):
        if ranks[i] == ranks[i+1] and \
                (i == 3 or ranks[i] != ranks[i+2]) and \
                (i == 0 or ranks[i] != ranks[i-1]):
            p = max(p, ranks[i])
    return p

def twopair(ranks, suits):
    p = []
    for i in range(4):
        if ranks[i] == ranks[i+1] and \
                (i == 3 or ranks[i] != ranks[i+2]) and \
                (i == 0 or ranks[i] != ranks[i-1]):
            p.append(ranks[i])
    if len(p) != 2: return None
    return p

def three(ranks, suits):
    for i in range(3):
        if ranks[i] == ranks[i+1] and ranks[i] == ranks[i+2]:
            return ranks[i]
    return None

def straight(ranks, suits):
    if ranks == [2, 3, 4, 5, 14]: return 5

    for i in range(4):
        if ranks[i]+1 != ranks[i+1]: return None
    return ranks[-1]

def flush(ranks, suits):
    if len(filter(lambda x: x == suits[0], suits)) != 5:
        return None
    return ranks[-1]

def full(ranks, suits):
    p = pair(ranks, suits)
    t = three(ranks, suits)
    if p is None or t is None: return None
    return (t, p)

def four(ranks, suits):
    if ranks[3] == ranks[0]: return ranks[0]
    if ranks[4] == ranks[1]: return ranks[4]
    return None

def straight_flush(ranks, suits):
    s = straight(ranks, suits)
    if s is None: return None
    f = flush(ranks, suits)
    if f is None: return None
    return ranks[-1]

def compare(hand1, hand2):
    a1 = sort(hand1)
    a2 = sort(hand2)

    x = straight_flush(*a1)
    if x:
        y = straight_flush(*a2)
        if not y: return 1
        if x > y: return 1
        if x < y: return 2
        return 0

    x = four(*a1)
    if x:
        if straight_flush(*a2): return 2
        y = four(*a2)
        if not y: return 1
        if x < y: return 2
        if x > y: return 1
        return kicker(a1[0], a2[0])

    x = full(*a1)
    if x:
        if straight_flush(*a2): return 2
        if four(*a2): return 2
        y = full(*a2)
        if not y: return 1
        return 1 if x[0] > y[0] else 2

    x = flush(*a1)
    if x:
        if straight_flush(*a2): return 2
        if four(*a2): return 2
        if full(*a2): return 2
        y = flush(*a2)
        if not y: return 1
        if x > y: return 1
        if x < y: return 2
        return kicker(a1[0], a2[0])

    x = straight(*a1)
    if x:
        if straight_flush(*a2): return 2
        if four(*a2): return 2
        if full(*a2): return 2
        if flush(*a2): return 2
        y = straight(*a2)
        if not y: return 1
        if x == y: return 0
        return 1 if x > y else 2
    
    x = three(*a1)
    if x:
        if straight_flush(*a2): return 2
        if four(*a2): return 2
        if full(*a2): return 2
        if flush(*a2): return 2
        if straight(*a2): return 2
        y = three(*a2)
        if not y: return 1
        if x > y: return 1
        return 2

    x = twopair(*a1)
    if x:
        if straight_flush(*a2): return 2
        if four(*a2): return 2
        if full(*a2): return 2
        if flush(*a2): return 2
        if straight(*a2): return 2
        if three(*a2): return 2
        y = twopair(*a2)
        if not y: return 1
        if x[1] > y[1]: return 1
        if x[1] < y[1]: return 2
        if x[0] > y[0]: return 1
        if x[0] < y[0]: return 2
        return kicker(a1[0], a2[0])

    x = pair(*a1)
    if x:
        if straight_flush(*a2): return 2
        if four(*a2): return 2
        if full(*a2): return 2
        if flush(*a2): return 2
        if straight(*a2): return 2
        if three(*a2): return 2
        if twopair(*a2): return 2
        y = pair(*a2)
        if not y: return 1
        if x > y: return 1
        if x < y: return 2
        return kicker(a1[0], a2[0])
    else:
        if straight_flush(*a2): return 2
        if four(*a2): return 2
        if full(*a2): return 2
        if flush(*a2): return 2
        if straight(*a2): return 2
        if three(*a2): return 2
        if twopair(*a2): return 2
        if pair(*a2): return 2    
        return kicker(a1[0], a2[0])
        
def name(hand):
    a = sort(hand)
    if straight_flush(*a): return 'Straight Flush'
    if four(*a): return 'Four of a Kind'
    if full(*a): return 'Full House'
    if flush(*a): return 'Flush'
    if straight(*a): return 'Straight'
    if three(*a): return 'Three of a Kind'
    if twopair(*a): return 'Two Pair'
    if pair(*a): return 'Pair'
    return 'High Card'

p1 = 0
p2 = 0
tie = 0
data = open('poker.txt').readlines()
for d in data:
    cards = d.strip().split(' ')
    h1 = cards[0:5]
    h2 = cards[5:]
    result = compare(h1, h2)
    if result == 1: p1 += 1
    if result == 2: p2 += 1
    if result == 0: tie += 1

print p1
