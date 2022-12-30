n,l = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [0]
a.sort()
# print(a)
if a[0]==0 and a[n-1]==l:
    for i in range(1,n):
        b.append(a[i]-a[i-1])
    print(max(b)/2)
if a[0]!=0 and a[n-1]==l:
    for i in range(1,n):
        b.append(a[i]-a[i-1])
    k = a[0]
    print(max(k,max(b)/2))
if a[0]==0 and a[n-1]!=l:
    for i in range(1,n):
        b.append(a[i]-a[i-1])
    k = l-a[n-1]
    print(max(k,max(b)/2))
if a[0]!=0 and a[n-1]!=l:
    for i in range(1,n):
        b.append(a[i]-a[i-1])
    k = a[0]
    j = l-a[n-1]
    print(max(j,k,max(b)/2))