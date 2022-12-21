for _ in range(int(input())):
    n =  int(input())
    a = [int(x) for x in input().split()]
    x = a[0]
    a.sort()
    for i in range(n):
        if x<a[i] and (x+a[i])%2!=0:
            x = (x+a[i])//2+1
        if x<a[i] and (x+a[i])%2==0:
            x = (x+a[i])//2
    print(x)