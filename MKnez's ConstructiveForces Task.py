for _ in range(int(input())):    
    n = int(input())
    if n==3:
        print("NO")
    else:
        print("YES")
        a = []
        if n%2!=0:
            for i in range(n):
                if i%2==0:
                    a.append(n//2-1)
                else:
                    a.append(-(n//2))
        else:
            for i in range(n):
                if i%2==0:
                    a.append(n)
                else:
                    a.append(-n)
        print(*a)