from fractions import Fraction
from functools import reduce
from math import gcd


def product(fracs):
    pro = fracs[0]
    for frac in fracs[1:]:
        pro *= frac
    t = reduce(gcd, [pro])
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
