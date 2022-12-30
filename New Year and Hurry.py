n,k = [int(x) for x in input().split()]
remain = 240-k
sum = 0
k1 = n+1
for i in range(n+1):
    sum = sum+5*i
    if remain<sum:
        k1 = i
        break
print(k1-1)