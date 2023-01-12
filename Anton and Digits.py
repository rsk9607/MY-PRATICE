a,b,c,d = [int(x) for x in input().split()]
k = 256*(min(a,c,d))
a = a-(min(a,c,d))
c = c-(min(a,c,d))
d = d-(min(a,c,d))
k = k+32*(min(a,b))
print(k)