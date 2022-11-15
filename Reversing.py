n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == 0:
        a[0:i] = a[0:i][::-1]
print(*a, sep=" ")

