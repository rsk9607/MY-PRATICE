n = int(input())
a = {4:0,7:0}
while n>0:
    a.setdefault(n%10,0)
    a[n%10]= a[n%10]+1
    n = n//10
t = 0
for x in a:
    if a[4]>0:
        if x!=4 or x!=7:
            t=1
        if a[4]+a[7]==4 or a[4]+a[7]==7:
            t=0
    elif a[4]==0:
        t=1
        if a[4]+a[7]==4 or a[4]+a[7]==7:
            t=0
if t==0:
    print("YES")
elif t==1:
    print("NO")