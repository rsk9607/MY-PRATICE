k = int(input())

for x in range(k+1):
    sumn = x*(x+1)*(x+2)//6
    if sumn == k:
        print(x)
        break
    elif sumn > k:
        print(x-1)
        break

