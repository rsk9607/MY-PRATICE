x = [int(a) for a in input().split()]
n = 0
x.sort()
for i in range(1,len(x)):
    if x[i-1] == x[i]:
        n = n+1
print(n)