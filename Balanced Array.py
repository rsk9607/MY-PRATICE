t = int(input())

while t > 0:
    n = int(input())
    a = []
    sum1 = 0
    sum2 = 0
    for x in range(2, n + 2, 2):
        a.append(x)
        sum1 = sum1 + x
    for y in range(1, n, 2):
        a.append(y)
        sum2 = sum2 + y
    if sum1 == sum2:
        print("YES")
        for i in range(0, n):
            print(a[i], end=" ")
