s = input()
a = list(s)
s = set(s)
b = []
count = 0
for x in s:
    b.append(a.count(x))
for x in b:
    if x ==1:
        count = count+1
    elif x>1:
        count = count+(x)*(x-1)+x
print(count)