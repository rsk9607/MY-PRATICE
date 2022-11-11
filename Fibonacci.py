# n = int(input())


# def fib(k):
#     if k == 1:
#         return 0
#     elif k == 2:
#         return 1
#     elif k > 2:
#         return fib(k - 1) + fib(k - 2)


# print(fib(n))

n = int(input())

a = [0,1]

for i in range(2,n):
    a.append(a[i-1]+a[i-2])

print(a[n-1])
