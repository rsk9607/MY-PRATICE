n,m = [int(x) for x in input().split()]
edge = []
for i in range(m):
    k = [int(x) for x in input().split()]
    k.sort()
    edge.append(k)
edge.sort()
count = 0
for i in range(len(edge)-2):
    if edge[i][0]==edge[i+1][0]:
        if edge[i+2][0]==edge[i][1] and edge[i+2][1]==edge[i+1][1]:
            count = count+1
    else:
        continue
print(count)
