a = []
n =int(input())
count =0
for _ in range(n):
    a.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(n):
        if a[i][1]==a[j][0]:
            count=count+1
print(count)