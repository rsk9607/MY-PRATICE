n = int(input())
a = list(map(int, input().split()))

a.sort()

if a[n-1] == 1:
    print("HARD")
else:
    print("EASY")