import math

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

t = int(input())
while t>0 :
    print(math.factorial( int(input())))
    t = t-1
