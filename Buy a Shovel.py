k,r =[int(x) for x in input().split()]
i = 1
while True:
    if (k*i-r)%10==0 or k*i%10==0:
        print(i)
        break
    else:
        i = i+1
