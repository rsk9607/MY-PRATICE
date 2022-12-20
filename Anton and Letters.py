s= input()
q = set()
for i in range(len(s)):
    if ord(s[i])>=97 and ord(s[i])<=122:
        q.add(s[i])
print(len(q))