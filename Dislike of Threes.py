for _ in range(int(input())):
    n = int(input())
    a = []
    i = 1
    while True:
        if i%3==0 or i%10==3:
            i = i+1
        else:
            a.append(i)
            i = i+1
        if len(a)==n:
            print(a[-1])
            break
    