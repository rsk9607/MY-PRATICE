for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    if a.count(max(a))==1:
        print(a.index(max(a))+1)
    elif a.count(min(a))==1:
        print(a.index(min(a))+1)