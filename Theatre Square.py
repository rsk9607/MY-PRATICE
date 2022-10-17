n,m,a = input().split()

n= int(n)
m= int(m)
a=int(a)

l=0
k=0


l=int(m/a)
k=int(n/a)
if(m%a)!=0 :
    l=l+1
if (n%a)!=0 :
    k=k+1
        
            

print(l*k)         