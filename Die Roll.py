from fractions import Fraction
r = [int(x) for x in input().split()]
po = 7-max(r)
to = 6
if po == to:
    print('1/1')
else:
    print(Fraction(po,to))
