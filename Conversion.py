s = input()
s = list(s)
for i in range(len(s)):
    if ord(s[i])>=97 and ord(s[i])<=122:
        s[i] = chr(ord(s[i])-32)
    elif ord(s[i])>=65 and ord(s[i])<=90:
        s[i] = chr(ord(s[i])+32)
    elif ord(s[i])==44:
        s[i] = chr(32)
s =''.join(map(str,s))
print(s)