n  = int(input())
s = input()
l = list(s)
for i in range(len(l)):
    if ord(l[i])>=97 and ord(l[i])<=122:
        l[i] = ord(l[i])-32
    else:
        l[i] =ord(l[i])
l = set(l)
if len(l)>=26:
    print("YES")
else:
    print("NO")