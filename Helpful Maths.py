s = input()
a = []
for i in range(len(s)):
    if s[i] != '+':
        a.append(int(s[i]))
a.sort()
for i in range(len(a)-1):
    print(a[i], end ="+")
else:
    print(a[-1])