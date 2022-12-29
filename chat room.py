s = input()
h = ['h','e','l','l','o']
l = 0
for i in range(len(s)):
    k = h[l]
    if s[i]==k:
        l = l+1
    if  s[i]==k and k == 'o':
        break
    
if  s[i]==k and k == 'o':
    print("YES")
else:
    print("NO")