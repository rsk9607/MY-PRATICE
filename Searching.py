n = int(input())
x = list(map(int, input().split()))
k = int(input())
for i in range(n):
    if x[i] == k:
        print(i)
        break
    else:
        print(-1)
        break
