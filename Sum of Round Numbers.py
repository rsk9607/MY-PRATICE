for _ in range(int(input())):
    n = int(input())
    a = []
    while n!=0:
        a.append(n%10)
        n = n//10
    for i in range(len(a)):
        a[i]=a[i]*pow(10,i)
    x=[i for i in a if i!=0]
    print(len(x))
    print(*x)
    