n = input()
n = list(n)

# count
A = 0  #cap
a = 0  #small
for i in range(len(n)):
    if ord(n[i])>=65 and ord(n[i])<=90:
        A = A+1
    elif ord(n[i])>=97 and ord(n[i])<=122:
        a = a+1

if A>a:
    for i in range(len(n)):
        if ord(n[i])>=65 and ord(n[i])<=90:
            continue
        elif ord(n[i])>=97 and ord(n[i])<=122:
            n[i]= chr(ord(n[i])-32)
else:
    for i in range(len(n)):
        if ord(n[i])>=65 and ord(n[i])<=90:
            n[i]= chr(ord(n[i])+32)
        elif ord(n[i])>=97 and ord(n[i])<=122:
            continue
l = ''.join([str(elem) for elem in n])
print(l)
