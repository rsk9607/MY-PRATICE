n = int(input())
x = [int(x) for x in input().split()]
count = x.index(max(x))
y = max(x)
x.remove(y)
x.insert(0,y)
x.reverse()
count = count + x.index(min(x))
print(count)


