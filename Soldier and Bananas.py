x, y, z = [int(a) for a in input().split()]
total = int(x*((z*(z+1))/2))
if total<y:
    print(0)
else:
    print(total-y)
