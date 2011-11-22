from types import GeneratorType

def generator(a, periodic):
    """ 
    Turn a sequence into an infinite generator by repeating the last
    entry. Alternatively, if the input is a generator, just yield the
    generator
    """
    if isinstance(a, GeneratorType):
        while True:
            yield a.next()

    if periodic:
        while True:
            for aa in a:
                yield aa
    else:
        for aa in a:
            yield aa

    while True:
        yield a[-1]

def convergent(a, b, periodic=False):
    """ 
    Return the convergents of the continued fraction
    b0+(a1/(b1+(a2/(...))))
    """
    a = generator(a, periodic)
    b = generator(b, periodic)
    b0 = b.next()
    b1 = b.next()
    a1 = a.next()
    a2 = a.next()

    A0 = b0
    B0 = 1
    yield A0, B0

    A1 = b1 * b0 + a1
    B1 = b1
    yield A1, B1

    while True:
        a2 = a.next()
        b2 = b.next()
        A2 = b2 * A1 + a2 * A0
        B2 = b2 * B1 + a2 * B0
        yield A2, B2
        A0, A1 = A1, A2
        B0, B1 = B1, B2
    
    
def root(num):
    """ 
    Return a generator for the sequences [b] for the continued
    fraction expansion of sqrt(n). That is, sqrt(n) = b0 + 1/(b1 +
    (1/...))
    """
    
    m0, d0 = 0, 1
    a0 = int(num**0.5)
    a00 = a0
    yield a0
    while True:
        m1 = d0 * a0 - m0
        d1 = (num - m1 ** 2) / d0
        a1 = int((a00 + m1) / d1)
        yield a1
        m0, d0, a0 = m1, d1, a1

def root_period(num):
    if int(num ** .5) ** 2 == num: return 0
    m0, d0 = 0, 1
    a0 = int(num**0.5)
    a00 = a0
    result = 0
    history = {}
    while True:
        m1 = d0 * a0 - m0
        d1 = (num - m1 ** 2) / d0
        a1 = int((a00 + m1) / d1)
        if (m1, d1, a1) in history:
            break
        result += 1
        history[(m1, d1, a1)] = 1
        m0, d0, a0 = m1, d1, a1
    return result

if __name__ == "__main__":
    a = root(114)
    for n,d in convergent([1], a):
        print 1. * n**2 / d**2 - 114
