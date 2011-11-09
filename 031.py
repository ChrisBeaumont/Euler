memo = {}

def change(num, mincoin=0):
    """ Finds number of unique coin combinations that add up to a given
    num.  To ensure all solutions are unique, we require that we add
    coins in non-decreasing order. The minimum acceptable coin
    denomination is set by mincoin"""

    # memoized result
    if (num, mincoin) in memo:
        return memo[(num, mincoin)]

    # base case -- only one way to sum up to zero
    if num == 0:
        return 1

    #add a coin, find number of ways to create
    #num - coin, aggregate
    result = 0
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        if num - coin < 0: continue
        if coin < mincoin: continue
        result += change(num - coin, coin)
    memo[(num, mincoin)] = result
    return result

print change(200)
