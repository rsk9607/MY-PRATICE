for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(n+1):
        a = set()
        while i>0:
            a.add(i%10)
            i //= 10
        if len(a) == 1:
            count += 1
    print(count)