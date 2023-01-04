import math 
for _ in range(int(input())):
    num = int(input())
    factors=[]
    for i in range(1,int(math.sqrt(num))):
        if num%i==0:
            factors.append(i)
    if len(factors)<3:
        print(-1)
    elif factors[1]==1 or factors[1]==num//factors[1] or num//factors[1]==1:
        print(-1)
    else:
        print(1,factors[1],num//factors[1])
    