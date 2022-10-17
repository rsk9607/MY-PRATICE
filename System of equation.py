import math

a = list(map(int, input().split()))

m = a[0]
n = a[1]

d1 = math.sqrt(4*m)
d2 = math.sqrt(4*n)

# root of equation

r1 = -(d1/(-2))
r2 = -(d2/(-2))

if r1 < n and r2 < m:
    print(1)
elif r1 == n or r2 == m:
    print(1)
else:
    print(0)
