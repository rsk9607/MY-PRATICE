n,k =  [int(x) for x in input().split()]
q = input()
l =  list(q)
for _ in range(k):
    i = 1
    while i<n:
        if l[i-1]=='B' and l[i]=='G':
            l[i-1] = 'G'
            l[i]='B'
            i = i+2
        else:
            i = i+1
print(''.join(map(str, l)))           