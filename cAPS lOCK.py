s = input()
k = 0
for i in range(1,len(s)):
    if ord(s[i]) >=97 and ord(s[i]) <=122:
       k=1
       break
    else:
        k=0
if k==0:
    for i in range(len(s)):
        if ord(s[i]) >=97 and ord(s[i]) <=122:
            s =s.replace(s[i],chr(ord(s[i])-32))
        elif ord(s[i]) >=65 and ord(s[i]) <=90:
            s = s.replace(s[i],chr(ord(s[i])+32))
    print(s)
elif k ==1:
    print(s)
