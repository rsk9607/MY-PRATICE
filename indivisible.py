for _ in range(int(input())):
    a,b,c = [int(x) for x in input().split()]
    for i in range(1,101):
        if a%i != 0 and b%i != 0 and c%i != 0:
            print(i)
            break
