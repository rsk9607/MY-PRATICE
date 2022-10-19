import math

t = int(input())

while t > 0:
    t = t-1
    n = int(input())
    while True:
        a = str(n)
        k = list(map(int, a))
        total = 0
        for i in range(len(k)):
            total = total + k[i]
        z = math.gcd(n, total)
        if z > 1:
            print(n)
            break
        else:
            n = n+1
