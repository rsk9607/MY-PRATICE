n = int(input())
a = [int(x) for x in input().split()]
b = {a[0]:1}
amaze = 0
for i in range(1,n):
    b.setdefault(a[i],0)
    b[a[i]]=b[a[i]]+1
    if b[max(b)]==1 and max(b)==a[i]:
        amaze=amaze+1
    elif b[min(b)]==1 and min(b)==a[i]:
        amaze=amaze+1
print(amaze)
        
    

    