dic = {}
for _ in range(int(input())):
    n =  input()
    if n not in dic:
        dic[n] = 1
    elif n in dic:
        dic[n] = dic[n]+1

v =  list(dic.values())
k = list(dic.keys())

print(k[v.index(max(v))])