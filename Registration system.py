a ={}
for _ in range(int(input())):
    s = input()
    a.setdefault(s,0)
    if a[s]==0:
        a.update({s:1})
        print("OK")
    elif a[s]>0:
        print(s+str(a[s]))
        a[s]=a[s]+1
