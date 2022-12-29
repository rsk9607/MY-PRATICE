a = int(input())
b = int(input())
c = int(input())
k1 = a+b*c
k2 = (b+c)*a
k3 = a*b*c
k4 = (a+b)*c
k5 = a+b+c
k6 = a*b+c
k8 = a*c+b
print(max(k1,k2,k3,k4,k5,k6,k8))