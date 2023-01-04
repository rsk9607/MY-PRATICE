n = int(input())
x = [int(a) for a in input().split()]
k = int(input())
try:
    print(x.index(k))
except:
    print(-1)
