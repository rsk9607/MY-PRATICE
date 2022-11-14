for _ in range(int(input())):
    x, y = [int(x) for x in input().split()]
    if x == y:
        print("Square")
    else:
        print("Rectangle")
