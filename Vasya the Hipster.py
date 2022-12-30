n,m = [int(x) for x in input().split()]
k1=min(m,n)
if m>n:
    m = m-n
    n = 0
    k2 = m//2
elif m<n:
    n = n-m
    m = 0
    k2 = n//2
elif m==n:
    k2=0
print(k1,k2)