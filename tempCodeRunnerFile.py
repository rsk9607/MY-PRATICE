m = 0
c = 0

for _ in range(int(input())):
    x, y = [int(x) for x in input().split()]
    m = m+x
    c = c+y

if m > c:
    print("Mishka")
elif m < c:
    print("Chris")
else:
    print("Friendship is magic!^^")