n = int(input())
a = [int(x) for x in input().split()]
b = []
j = 0
for i in range(1,n):
    if a[i-1]<=a[i]:
        j = j+1
    if a[i-1]>a[i]:
        b.append(j+1)
        j = 0
b.append(j+1)
print(max(b))