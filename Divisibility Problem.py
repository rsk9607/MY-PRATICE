for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    if a%b != 0:
        print(b- a%b)
    else:
        print(0)