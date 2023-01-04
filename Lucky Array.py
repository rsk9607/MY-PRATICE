n = int(input())
a = [int(x) for x in input().split()]
if a.count(min(a))%2!=0:
    print("Lucky")
elif a.count(min(a))%2==0:
    print("Unlucky")