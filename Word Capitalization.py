word = input()
l = list(word)
if ord(l[0])>=97 and ord(l[0])<=122:
    l[0] = chr(ord(l[0])-32)
str1 = ''.join(l)
print(str1)