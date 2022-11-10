for _ in  range(int(input())):
    a, b = [int(x) for x in input().split()]
    m1 = max(a,b)
    m2 = min(a,b)
    if 2*m2 > m1:
        s = 2*m2
    elif 2*m2 <= m1:
        s = m1
    print(s*s)