n = int(input())
a = [int(x) for x in input().split()]
b = a.copy()
b.reverse()
if a == b:
    print("YES")
else:
    print("NO")