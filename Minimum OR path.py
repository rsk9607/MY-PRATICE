for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = []
    i = 0
    while i<n:
        for j in range(i,min(i+a[i],n)+1):
            if j<n:
                i=j
        b.append(a[i])
    print(b)