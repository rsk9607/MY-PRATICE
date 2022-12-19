n = int(input())
a = []

for i in range(0,n):
    k = int(input())
    a.append(k)
g = 1 
for i in range(1,n):
    if a[i-1] != a[i]:
        g = g+1
print(g)