n = int(input())

a = list(map(int,input().strip().split()))[:n]
b = list(map(int,input().strip().split()))[:n]

a.sort()
b.sort()

if a==b:
    print("yes")
else:
    print("no")