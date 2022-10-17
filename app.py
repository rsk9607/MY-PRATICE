t = int(input())

while t>0 :
    t=t-1
    a = list(map(int, input().split()))
    c = max(a[0],a[1])
    d = max(a[2],a[3])
    m = max(c,d)
    n = min(c,d)
    a.sort()
    b = a
    if m==b[3] and n==b[2] :
        print("YES")
    else :
        print("NO")


