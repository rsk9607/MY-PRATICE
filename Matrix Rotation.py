row = 2
a = []
for i in range(row):
    a.append([int(x) for x in input().split()])
k = 0 
while a[0][0]>a[0][1] or a[1][0]>a[1][1] or a[0][0]>a[1][0] or a[0][1]>a[1][1]:
    k = k+1
    for i in range(2):
        for j in range(2):
            