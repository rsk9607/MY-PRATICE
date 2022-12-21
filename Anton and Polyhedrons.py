k = 0
for _ in range(int(input())):
    s= input()
    if s[0]=='T':
        k=k+4
    elif s[0] =='C':
        k=k+6
    elif s[0] =='O':
        k=k+8
    elif s[0] =='D':
        k=k+12
    elif s[0] =='I':
        k=k+20
print(k)