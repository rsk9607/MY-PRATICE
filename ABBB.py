for _ in range(int(input())):
    s = input()
    s = list(s.split())
    for i in range(1, len(s)):
        if s[i - 1] == 'A' and s[i] == 'B':
            s.pop(i - 1)
            s.pop(i)
            continue
        if s[i - 1] == 'B' and s[i] == 'B':
            s.pop(i - 1)
            s.pop(i)
            continue
    print(len(s))
