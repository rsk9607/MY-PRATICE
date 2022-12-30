n = int(input())
a = [int(x) for x in input().split()]
k1 = a.count(1)
k2 = a.count(2)
k3 = a.count(3)
k4 = a.count(4)
cab = k4+k3
if k1>k3:
    k1 =k1-k3
else:
    k1 =0
cab = cab+k2//2
k2 =k2%2
cab = cab+k1//4
k1 =k1%4
if k2 ==1:
    if k1 ==3:
        cab =cab +2
    elif k1 ==2:
        cab = cab+1
    elif k1 ==1:
        cab = cab+1
    elif k1 ==0:
        cab = cab+1
if k2 ==0:
    if k1>0:
        cab = cab+1
print(cab)


    