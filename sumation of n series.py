t = int(input())
m = 1000000007

for i in range(t):
  x = int(input())
  x = x*x
  x = x%m
  print(x)

  #why mod???
