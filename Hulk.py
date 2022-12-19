n = int(input())
s = "I hate"
for i in range(2,n+1):
    if i%2 == 0:
        s = s + " that I love"
    elif i%2 != 0:
        s = s + " that I hate"
s = s+ " it"
print(s)