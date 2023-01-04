for _ in range(int(input())):
    n = int(input())
    a = input()
    if len(set(a))==1:
        print(-1)
    else:
        for i in range(1,n):
            if a[i-1]=='L' and a[i]=='R':
                print(i)
                break
        else:
            print(0)