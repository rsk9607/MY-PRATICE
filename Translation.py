s = input()
t = input()

t = "".join(reversed(t))

if s == t:
    print("YES")
else:
    print("NO")
