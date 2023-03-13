n,k=[int(x) for x in input().split()]
a = [int(x) for x in input().split()] 
b = []
for i in range(n):
    if a[i]<=(5-k):
        b.append(a[i])
print(len(b)//3)