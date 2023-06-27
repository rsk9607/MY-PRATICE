for _ in range(int(input())):
    n =  int(input())
    if n%2 != 0:
        print('YES')
        continue
    else:
        while n%2 == 0:
            n //= 2
        if n%2 != 0 and n != 1:
            print("YES")
        else:
            print('NO')