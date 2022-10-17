n, k = map(int, input().split())
a = []
if n%2 == 0:
    for x in range(1, n, 2):
        a.append(x)
    for y in range(2, n+2, 2):
        a.append(y)
else:
    for x in range(1, n+2, 2):
        a.append(x)
    for y in range(2, n, 2):
        a.append(y)
print(a[k-1])
