tri = [.5 * n * (n+1) for n in range(1, 1000)]
tri = dict(zip(tri, tri)) # store in dictionary for fast lookup

def tri_word(word):
    sum = 0
    offset = ord('A')
    for letter in word:
        sum += ord(letter) - offset + 1 #ranking of each letter
    return sum in tri

words = open('words.txt').read().replace('"', '').split(',')
words = filter(tri_word, words)
print len(words)
