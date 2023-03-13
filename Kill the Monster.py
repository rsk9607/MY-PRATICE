for _ in range(int(input())):
    hc, dc = [int(x) for x in input().split()]
    hm, dm = [int(y) for y in input().split()]
    k, w, a = [int(z) for z in input().split()]
    flag = False
    i = 0
    while i<=k:
        hc = hc + i*a
        dc = dc +(k-i)*w
        i = i+1
        j = 1
        while hc>0 and hm>0:
            if j%2 == 0:
                hc = hc - dm
            elif j % 2 != 0:
                hm = hm - dc
            j = j+1
        if hc>hm:
            flag = True
            break
        elif hc < hm:
            continue    
    if flag:
        print("YES")
    else:
        print("NO")