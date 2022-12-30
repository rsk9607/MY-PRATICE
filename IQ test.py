n = int(input())
a = [int(x) for x in input().split()]
ce = 0
co = 0
for x in a:
    if x%2 == 0:
        ce = ce+1
    elif x%2 !=0:
        co = co+1
if ce ==1:
    for x in a:
        if x%2 == 0:
            print(a.index(x)+1)
elif co ==1:
    for x in a:
        if x%2 !=0:
            print(a.index(x)+1)
