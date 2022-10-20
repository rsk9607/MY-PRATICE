t = int(input())

while t > 0:
    t = t-1
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = sum(a)
    y = sum(b)
    for i in range(n):
        k1 = 0
        l2 = 0
        if x == y:
            if a[i] > b[i]:
                k1 = a[i] + k1
                l2 = 0 + l2
            else:
                l2 = b[i] + l2
                k = 0 + k1
    print(min(l2, k1))
