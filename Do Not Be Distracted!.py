for _ in range(int(input())):
    n =  int(input())
    s = input()
    dic = {}
    k=1
    if len(s) == 1:
        print('YES')
        continue
    for i in range(len(s)):
        if s[i] in dic and s[i]==s[i-1]:
            k = 1
            dic[s[i]]= dic[s[i]]+1
        elif s[i] in dic and s[i]!=s[i-1]:
            k = 0
            break
        elif s[i] not in dic:
            dic[s[i]] = 1
    if k==0:
        print('NO')
    else:
        print('YES')
