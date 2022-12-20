for _ in range(int(input())):
    a,b = [str(x) for x in input().split()]
    if a[-1] == b[-1] and a.count('X') == b.count('X'):
        print("=")
    elif a[-1] == b[-1] and a.count('X') > b.count('X') and a[-1] =="S":
        print("<")
    elif a[-1] == b[-1] and a.count('X') < b.count('X') and a[-1] =="S":
        print(">")
    elif a[-1] == b[-1] and a.count('X') > b.count('X') and a[-1] =="L":
        print(">")
    elif a[-1] == b[-1] and a.count('X') < b.count('X') and a[-1] =="L":
        print("<")
    if a[-1] != b[-1]:
        if  a[-1] == 'S' and b[-1] =='M':
            print("<")
        elif a[-1] == 'S' and b[-1] =='L':
            print("<") 
        elif a[-1] == 'M' and b[-1] =='L':
            print("<")
        elif a[-1] == 'M' and b[-1] =='S':
            print(">")
        elif a[-1] == 'L' and b[-1] =='M':
            print(">")
        elif a[-1] == 'L' and b[-1] =='S':
            print(">")