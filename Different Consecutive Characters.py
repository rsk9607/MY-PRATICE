t = int(input())

while t > 0:
    t = t-1
    a = int(input())
    n = input()
    count = 0
    i = 1
    while i < a:
        if n[i-1] == n[i]:
            count == count + 1
        i = i+1
    print(count)
    