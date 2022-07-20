from collections import Counter
for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))

    ac = Counter(a)
    nb = 0

    l = []
    lv = []
    for key, val in ac.items():
        nb += 1
        l.append(key)

    for i in range(1, 101):
        if len(l) < k:
            if i not in l:
                l.append(i)
        else:
            break

    if len(l) < k:
        print(-1)
    else:
        if nb > k:
            print(-1)
        else:
            print(n*len(l))
            for i in range(n):
                print(*l, end=' ')
            print('')
