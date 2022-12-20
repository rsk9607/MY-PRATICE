s = input()
k = ""
for i in range(len(s)):
    if s[i] != "a" and s[i] != "e" and s[i] != "i" and s[i] != "o" and s[i] != "u" and s[i] != "y" and s[i] != "A" and s[i] != "E" and s[i] != "I" and s[i] != "O" and s[i] != "U" and s[i] != "Y":
        if ord(s[i])>=97 and ord(s[i])<=122:
            k = k+"."+s[i]
        else:
            k = k+"."+chr(ord(s[i])+32)
print(k)