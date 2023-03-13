n =input()
a = []
i=0
while i<len(n) :
    if n[i]=='-':
        if n[i+1]=='.':
            a.append(1)
        elif n[i+1]=='-':
            a.append(2)
        i=i+2
    elif n[i]=='.':
        a.append(0)
        i=i+1
print(*a, sep="")
    