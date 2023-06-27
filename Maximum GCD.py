for _ in range(int(input())):
    n = int(input())
    if n%2 == 0:
        print(n//2)
    elif n ==1:
        print(n)
    elif n%2 != 0:
        print((n-1)//2)