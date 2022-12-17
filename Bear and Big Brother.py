a, b = [int(x) for x in input().split()]
i = 0
while a<=b :
    i = i+1
    a = 3*a
    b = 2*b
    if a>b:
        break
print(i)