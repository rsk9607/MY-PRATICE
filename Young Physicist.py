# no of rows & cols

rows = int(input())
a = []
for i in range(rows):
    b = list(map(int, input().split()))
    a.append(b)
sx = 0
sy = 0
sz = 0
for i in range(rows):
    sx =sx+ a[i][0]
    sy =sy +a[i][1]
    sz =sz +a[i][2]
if sz == 0 and sx == 0 and sy == 0:
    print("YES")
else:
    print("NO")
    