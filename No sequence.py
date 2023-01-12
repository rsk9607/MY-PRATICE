for _ in range(int(input())):
    n,k,s = [int(x) for x in input().split()]
    b = []
    a = []
    for i in range(n):
        a.append(pow(k,i))
    print(a)
    for i in range(1,n+1):
        if s-a[-i]>=0:
            b.append(1)
        if s-a[-i]<0:
            b.append(0)
    print(b)