p = 0
k = []
for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    p = p-a+b
    k.append(p)
print(max(k))