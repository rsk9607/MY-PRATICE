m = 0
c = 0

for _ in range(int(input())):
    x, y = [int(x) for x in input().split()]
    if x > y:
        m = m + 2
    elif x < y:
        c = c + 2
    elif x == y:
        m = m + 1
        c = c + 1
if m > c:
    print("Mishka")
elif m < c:
    print("Chris")
elif m == c:
    print("Friendship is magic!^^")
