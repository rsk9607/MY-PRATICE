# no of rows & cols

rows = int(input())
cols = int(input())

a = []
i = 0
while i < rows:
    i = i + 1
    b = list(map(int, input().split()))
    a.append(b)

print(a)
print(a[0][1])
