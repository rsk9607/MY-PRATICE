n = int(input())
a = list(map(int, input().strip().split()))[:n]
a.sort()
count = 0
for i in range(n):
    if a[i] != a[n-1]:
        count = a[n-1]-a[i] + count
print(count)