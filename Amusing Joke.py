s1 = input()
s2 = input()
s3 = input()
s4 = s1+s2
s3 =''.join(sorted(s3))
s4 =''.join(sorted(s4))
if s3 == s4:
    print("YES")
else:
    print("NO")