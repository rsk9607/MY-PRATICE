for _ in range(int(input())):
    s = input()
    s1=0
    s2=0
    for i in range(0,len(s)//2):
        s1 = s1+int(s[i])
        s2 = s2+int(s[-i-1])
    if s1==s2:
        print('YES')
    else:
        print('NO')
        
    