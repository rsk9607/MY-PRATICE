for _ in range(int(input())):
    n =  int(input())
    s = input()
    dic = {}
    k=0
    for i in range(len(s)-1):
        if s[i] in dic and s[i]==s[i-1]:
            k = 1
            dic[s[i]]= dic[s[i]]+1
        elif s[i] in dic and s[i]!=s[i-1]:
            k=0
        elif s[i] not in dic:
            dic[s[i]] = 1
    if k==0:
        print('NO')
    else:
        print('YES')
