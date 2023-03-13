for _ in range(int(input())):
    x,y =[int(x) for x in input().split()]
    n = 0
    while True:
        if (n+x)%y==0 and (n+y)%x==0:
            print(n)
            break
        else:
            n = n+1