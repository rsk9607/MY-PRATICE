a,b = [int(x) for x in input().split()]
time = a
rem = a
while a>0:
    a = rem//b
    rem = rem%b
    time = time + a
    rem = rem + a
print(time)