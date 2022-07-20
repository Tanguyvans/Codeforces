from collections import Counter

for _ in range(int(input())):

    n = int(input())
    s = list(map(int, input().split(' ')))

    a = {}

    for i in range(n):
        if s[i] in a:
            a[s[i]].append(i)
        else:
            a[s[i]] = [i]

    flag = False
    sol = {}
    for k, v in a.items():
        if len(v) == 1:
            flag = True
            break
        else:
            for i in range(len(v)-1):
                sol[v[i]] = v[i+1]
            sol[v[-1]] = v[0]

    if flag:
        print(-1)
    else:
        for i in range(n):
            print(sol[i]+1, end=' ')
        print('')
