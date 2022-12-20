for _ in range(int(input())):
    n = int(input())
    a = input()
    s = ""
    count = (a.count('1'))//2
    for i in range(1,n):
        if a[i] =='0':
            s = s + "+"
        while a[i] == '1':
            if count>0:
                s = s + "-"
                count = count -1
                break
            else:
                s = s+ "+"
                break        
    print(s)