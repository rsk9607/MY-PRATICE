n = int(input())
a = [int(x) for x in input().split()]
i = 0
s = 0
d = 0
while len(a)>0:
    if i%2==0:
        s = s+max(a[-1],a[0])
        a.remove(max(a[-1],a[0]))
    if i%2!=0:
        d = d+max(a[-1],a[0])
        a.remove(max(a[-1],a[0]))
    i = i+1
print(s,d)