n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
for _ in range(int(input())):
    c,b = [int(x) for x in input().split()]
    x = a[c-1:b]
    if len(x)>n-k+1 and x[-1]!=0:
        print("No")
        continue
    else:
        print("Yes")