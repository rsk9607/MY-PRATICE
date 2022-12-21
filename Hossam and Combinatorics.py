for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    if max(a)!=min(a):
        l = a.count(max(a))
        m = a.count(min(a))
        k = 2*l*m
        print(k)
    elif max(a)==min(a):
        print(n*(n-1))