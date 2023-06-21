for _ in range(int(input())):
    s =  input()
    k = []
    k[:0] = s
    
    for i in range(1,len(k)):
        if k[i] == k[i-1] and i!=0 and i!=len(k)-1:
            k[i] = "0"
    k = [x for x in k if x != '0']
    print(*k,sep='')