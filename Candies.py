for _ in range(int(input())):
    n = int(input())
    x = 0
    for k in range(2,n):
        x = n/(pow(2,k)-1)
        y = int(x)
        if y-x==0:
            print(y)
            break
        