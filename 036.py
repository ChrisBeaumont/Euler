def binary(x):
    result = []
    while(x != 0):
        result.append(str(x % 2))
        x /= 2
    return ''.join(result)

def is_palindrome(x):
    s = str(x)
    if s != s[::-1]: return False
    s = binary(x)
    return s == s[::-1]

numbers = xrange(1, 1000000)
result = filter(is_palindrome, numbers)

print sum(result)    
