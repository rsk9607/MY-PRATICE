n = int(input())
x = [int(a) for a in input().split()]
y = [int(a) for a in input().split()]
a = x[0]
b = y[0]
x.remove(x[0])
y.remove(y[0])
# print(x)
# print(y)
x = set(x)
y = set(y)
z = x.union(y)
if len(z) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")