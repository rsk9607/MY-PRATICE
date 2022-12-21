for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    l = []
    for x in range(max(a,b)+1):
        l.append((a ^ x)+(b ^ x))
    print(min(l))