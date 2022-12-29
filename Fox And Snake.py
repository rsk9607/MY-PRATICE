m,n = [int(x) for x in input().split()]
for i in range(m):
    s =""
    if (i+1)%2 != 0:
        for j in range(n):
            s =s+"#"
        print(s)
        continue
    if (i+1)%4 == 0:
        for j in range(n):
            if j == 0:
                s = s+"#"
            if j != 0:
                s = s+"."
        print(s)
        continue
    if (i+1)%4 != 0:
        for j in range(n):
            if j ==(n-1):
                s = s+"#"
            if j !=(n-1):
                s = s+"."
        print(s)
        continue    