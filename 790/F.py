from collections import Counter

for _ in range(int(input())):

    n, k = map(int, input().split(' '))

    a = list(map(int, input().split(' ')))
    a = sorted(a)
    ct = Counter(a)

    l = 0
    r = 0

    b = []

    for key, value in ct.items():
        if value >= k:
            b.append(key)

    if len(b) > 0:
        l = 0
        ans = 0
        inter = 0
        li = b[0]
        for i in range(len(b)-1):
            if b[i]+1 == b[i+1]:
                inter += 1
            else:
                ans = max(ans, inter)
                if ans == inter:
                    l = li

                inter = 0
                li = b[i+1]

        ans = max(ans, inter)
        if ans == inter:
            l = li

        if ans >= 0:
            print(l, l+ans)
        else:
            print(-1)
    else:
        print(-1)
