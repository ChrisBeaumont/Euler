# for all x, f(x) <= 9^5 ceil(log(x))
# this allows us to stop searching at x >= 9^5 ceil(log(x))

top = 370001
terms = []
for i in range(10, top):
    if i == sum([int(x) ** 5 for x in str(i)]):
        terms.append(i)

print sum(terms)
