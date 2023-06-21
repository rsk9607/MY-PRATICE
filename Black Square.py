c1,c2,c3,c4 = [int(x) for x in input().split()]
s = input()
cal = 0
for x in s:
    if x =='1':
        cal = cal + c1
    elif x=='2':
        cal = cal+c2
    elif x=='3':
        cal = cal + c3
    elif x=='4':
        cal = cal+c4
print(cal)