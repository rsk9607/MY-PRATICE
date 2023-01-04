for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    h = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    # l= max(h)/k
    # if l%1!=0:
    #     l =max(h)//k+1
    # else:
    #     l =max(h)//k
    # q = k/min(p)
    # if q%1!=0:
    #     q = k//min(p)+1
    # else:
    #     q = k//min(p)
    # if l<=q:
    #     print("YES")
    # elif l>q:
    #     print("NO")
    while max(h)<=0 or k<=0:
        
        