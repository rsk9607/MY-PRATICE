n,m = [int(x) for x in input().split()]
a = set()
for i in range(n):
    b = [str(x) for x in input().split()]
    b = set(b)
    a.update(b)
a = list(a)
for i in range(len(a)):
    if a[i] !="W" and a[i] !="B" and a[i] !="G":
        s ="#Color"
        break
    else:
        s= "#Black&White"
print(s)