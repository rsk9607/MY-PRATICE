s = input()
l = "NO"
for i in range(len(s)):
    if s[i]=='H' or s[i] =='Q' or s[i] == '9':
        l = "YES"
        break
    else:
        l = "NO"
print(l)
