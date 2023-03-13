for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if n==1:
        print("YES")
        continue
    elif n>1:
        for i in range(1,n):
            s =0
            if a[i]-a[i-1]>1:
                s=1
                break
        if s==0:
            print("YES")
        else:
            print("NO")
            