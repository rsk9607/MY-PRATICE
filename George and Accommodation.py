c = 0
for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    if b-a >= 2:
        c = c+1
print(c)