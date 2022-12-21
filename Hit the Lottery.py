n = int(input())
k = 0
k = k+ n//100
n = n%100
k = k+n//20
n = n%20
k = k+n//10
n = n%10
k = k+n//5
n = n%5
k = k+n//1
n =n%1
print(k)
