import math
for _ in range(int(input())):
    n,m = [int(x) for x in input().split()]
    print(math.gcd(n,m))