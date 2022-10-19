n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
count = 0
for i in range(n):
    a[i].sort()
    if a[i][1] == 1 and a[i][2] == 1:
        count = 1 + count

print(count)
