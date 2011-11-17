from util import gcd

class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        #self.reduce()

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.denom + other.num * self.denom, 
                            self.denom * other.denom)
        return Fraction(self.num + int(other) * self.denom, self.denom)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.denom * other.denom)
        return Fraction(self.num * int(other), self.denom)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.denom, self.denom * other.num)
        return Fraction(self.num, int(other) * self.denom)

    def __rdiv__(self, other):
        if isinstance(other, Fraction):
            return other.__div__(self)
        return Fraction(int(other) * self.denom, self.num)

    def reduce(self):
        x = gcd(self.num, self.denom)
        self.num /= x
        self.denom /= x

    def whole(self):
        return (self.num % self.denom) == 0

    def int(self):
        if not self.whole():
            raise ValueError("Fraction not a whole number: %s" % self)
        return self.num / self.denom

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denom >= self.denom * other.num
        return self.num * other >= self.denom

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denom > self.denom * other.num
        return self.num * other > self.denom


    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denom <= self.denom * other.num
        return self.num * other <= self.denom


    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denom < self.denom * other.num
        return self.num * other < self.denom


    def __str__(self):
        self.reduce()
        return "%i/%i" % (self.num, self.denom)
        
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denom == self.denom * other.num
        else:
            return self.whole() and self.int() == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        if self.num > self.denom:
            return 391358313 * self.num / self.denom
        else:
            return 391358313 * self.denom / self.num
