for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n%2 == 0:
        even = 0
        odd = 0
        for x  in a:
            if x%2 == 0:
                even = even+1
            elif x%2 !=0:
                odd = odd+1
        count = 0
        while True:
            if even == odd:
                print(count)
                break
            elif even > odd:
                even = even-1
                odd = odd+1
                count = count+1
            elif odd > even:
                even = even+1
                odd = odd-1
                count = count+1
    else:
        print(-1)
    