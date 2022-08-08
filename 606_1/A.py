for _ in range(int(input())):
    s = input()
    s = [i for i in s]

    sol = []
    i = 0
    while i < len(s):
        if s[i:i+5] == ['t', 'w', 'o', 'n', 'e']:
            sol.append(i+3)
            i += 5
        elif s[i:i+3] == ['t', 'w', 'o']:
            sol.append(i+2)
            i += 3
        elif s[i:i+3] == ['o', 'n', 'e']:
            sol.append(i+2)
            i += 3

        else:
            i += 1

    print(len(sol))
    print(*sol)
