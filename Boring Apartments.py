for _ in range(int(input())):
    a = int(input())
    n = a
    k = 0
    r = n%10
    ans = 10*(r-1)
    while n%10 != 0:
        k = k+1
        n = n//10
    ans = ans + (k*(k+1))//2
    print(ans)