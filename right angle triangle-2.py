n = int(input())

l1 = 0

for i in range(1, n+1):
    k = 0
    while k < i:
        if k == 0:
            l1 = i
        else:
            l1 = l1+n-k
        print(l1, end=" ")
        k = k + 1
    print("")
