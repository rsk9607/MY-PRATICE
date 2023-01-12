def check(l,k):
    i = 1 
    while l>=0 and l<2*l:
        k.append(l)
        if i%2==0:
            l = l-i
        elif 1%2!=0:
            l = l+i
        i = i+1
    return k
    

k = int(input())
a = [0]
a = check(k,a)
print(a)
a.sort()
print(a)
