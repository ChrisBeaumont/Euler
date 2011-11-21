from types import GeneratorType

def generator(a):
    """ 
    Turn a sequence into an infinite generator by repeating the last
    entry. Alternatively, if the input is a generator, just yield the
    generator
    """
    if isinstance(a, GeneratorType):
        while True:
            yield a.next()

    for aa in a:
        yield aa

    while True:
        yield a[-1]

def convergent(a, b):
    """ 
    Return the convergents of the continued fraction
    b0+(a1/(b1+(a2/(...))))
    """
    a = generator(a)
    b = generator(b)
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
    
    

