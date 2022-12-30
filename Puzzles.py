n,m =[int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = []
a.sort()
for i in range(m-n+1):
    b.append(a[i+n-1]-a[i])
print(min(b))