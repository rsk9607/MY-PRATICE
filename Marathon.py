for _ in range(int(input())):
    a = [int(x) for x in input().split()]
    count = 0
    for i in range(len(a)):
        if a[i] > a[0]:
            count = count +1
    print(count)