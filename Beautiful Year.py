y = input()
a = int(y)
a = a+1
y = str(a)
while True :
    if y[0] != y[1] and y[0] != y[2] and y[0] != y[3] and y[1] != y[2] and y[1] != y[3] and y[2] != y[3]:
        print(a)
        break
    else:
        a = a+1
        y = str(a)
