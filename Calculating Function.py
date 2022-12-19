n = int(input())
if n%2 == 0:
    k = n//2
    print((k*(k+1))-(k*k))
elif n%2 != 0:
    k1 = n//2 #even
    k2 = n//2+1 #odd
    print((k1*(k1+1))-(k2*k2))