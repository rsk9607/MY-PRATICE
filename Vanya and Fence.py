n,h =[int(x) for x in input().split()]
a = [int(a) for a in input().split()]
row = 0
for i in range(n):
    if a[i]>h:
        row =  row + 2
    elif a[i]<=h:
        row =  row + 1
print(row)
