x = 0
for _ in range(int(input())):
    s = input()
    if s[1]=="+":
        x = x+1
    elif s[1] == "-":
        x = x-1
print(x)