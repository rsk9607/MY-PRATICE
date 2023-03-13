n,k = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append(input())
b = a[0:k]
b.sort()
for i in range(k):
    print(b[i])