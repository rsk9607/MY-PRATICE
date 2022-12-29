for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    while(a[-2] != 1):
        a[-1] = a[-1]*a[-2]
        a[-2] = 1
        a.sort()
    print(2022*sum(a))
