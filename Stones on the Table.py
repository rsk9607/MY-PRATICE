n = int(input())
s = input()
a = list(s.strip())
i = 1
k = 0
while i<len(a):
    if a[i-1] == a[i]:
        a.pop(i)
        k = k+1
        i = 1
    else:
        i= i+1
print(k)