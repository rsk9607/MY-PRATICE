t = int(input())

while t > 0:
    t = t-1
    a = list(map(int, input().split()))
    if a[0]%2==0 and a[1]%2==0 and a[2]%2==0:
        print("NO")
    elif a[0]%2!=0 and a[1]%2!=0 and a[2]%2!=0:
        print("NO")
    else:
        print("YES")
