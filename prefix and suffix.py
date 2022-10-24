string = input()
length = len(string)
half = length//2
for i in range(half, 0, -1):
    prefix = string[0:i]
    suffix = string[length-i-1:length-1]
    if prefix == suffix:
        print(len(prefix))
        break
