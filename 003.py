def primefactors(num):
    result = []
    for div in xrange(2, num+1):
        if div > num: break
        if num % div != 0: continue
        result.append(div)
        while (num % div) == 0:
            num /= div
    return result

print max(primefactors(600851475143))
            
    
