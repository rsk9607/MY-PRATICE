n = int(input())
a = [int(x) for x in input().split()]
for i in range(n):
    if a[i]>0:
        a[i]=1
    elif a[i]<0:
        a[i]=2
    elif a[i]==1:
        a[i]=0
print(*a)