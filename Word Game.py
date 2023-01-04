for _ in range(int(input())):
    n =  int(input())
    a = [str(x) for x in input().split()]
    b = [str(x) for x in input().split()]
    c = [str(x) for x in input().split()]
    a1 = 0
    b1 = 0
    c1 = 0
    for i in range(n):
        if a[i]==b[i] and b[i]==c[i] and  a[i]==c[i]:
            a1 = a1
            b1 = b1
            c1 = c1
            continue
        if a[i]!=b[i] and b[i]!=c[i] and  a[i]!=c[i]:
            a1 = a1+3
            b1 = b1+3
            c1 = c1+3
            continue
        if a[i]==b[i] and b[i]!=c[i] and a[i]!=c[i]:
            a1 = a1+1
            b1 = b1+1
            c1 = c1+3
            continue
        if a[i]!=b[i] and b[i]==c[i] and a[i]!=c[i]:
            a1 = a1+3
            b1 = b1+1
            c1 = c1+1
            continue
        if a[i]!=b[i] and b[i]!=c[i] and a[i]==c[i]:
            a1 = a1+1
            b1 = b1+3
            c1 = c1+1
            continue
    print(a1,b1,c1)