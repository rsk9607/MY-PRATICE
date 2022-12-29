n = int(input())
a = [int(x) for x in input().split()]
p = 0
count = 0
for x in a:
    if x == -1:
        if p+x<0:
            count = count+1
        else:
            p = p+x
            continue
    if x != -1:
        p = p+x
print(count)