n,m = [int(z) for z in input().split()]
a=[int(z) for z in input().split()]
c = [int(z) for z in input().split()]
req = [int(z) for z in input().split()]
j = req[-1]
cost = a[req[-1]-1]+c[req[-1]]
req.remove(req[-1])
while len(req)>0:
    for i in range(len(a)):
        temp = 0
        
