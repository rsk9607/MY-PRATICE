n = int(input().strip())
p = list(map(int, input().strip().split()))
for i in range(n):
  print(p.index(i + 1) + 1, end=" ")
