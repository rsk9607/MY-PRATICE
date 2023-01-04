a = input()
b = input()
print(len(a),len(b))
c = a+b
print(c)
a= list(a)
b = list(b)
k =a[0]
a[0]=b[0]
b[0]=k
a = ''.join(map(str,a))
b = ''.join(map(str,b))
print(a,b)