for _ in range(int(input())):
    n,x = [int(k) for k in input().split()]
    floor = 0
    if n ==1 or n==2:
        floor = 1
    else:
        if (n-2)%x != 0:
            floor = (n-2)//x +2
        else:
            floor = (n-2)//x +1
    print(floor)