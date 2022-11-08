for _ in range(int(input())):
    x, y, n = [int(x) for x in input().split()]
    q1 = n//x
    r1 = n%x
    if y<r1:
        print(q1*x+y)
    elif y>r1:
        print((q1-1)*x+y)
    else :
        print(n)
    