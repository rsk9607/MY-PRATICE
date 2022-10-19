n = input()
m = input()

a = []
for i in range(len(m)):
    if n[i] == m[i]:
        a.append(0)
    else:
        a.append(1)

print(''.join(map(str, a)))
