for _ in range(int(input())):
    n,y = [int(x) for x in input().split()]
    a = [int(x) for  x in input().split()]
    k = 0
    for i in range(n):
        k = k|a[i]
    i = 0
    z = 0
    x = k
    while x|z != y:
        if y&(1<<i)>=1 and x&(1<<i)==0:
            z = z|(1<<i)
        elif x&(1<<i)>=1  and y&(1<<i)==0:
            z = -1
            break
        i = i+1
    print(z)
    