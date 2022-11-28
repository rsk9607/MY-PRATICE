for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    n = 0
    while True:
        if n*n >= 2*a*b :
            print(n*n)
            break
        n = n+1