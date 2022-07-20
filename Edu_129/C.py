for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    c = [int(i) for i in range(n)]
    ab = zip(c, a, b)
    sab = sorted(ab, key=lambda ab: (ab[1], ab[2]))
    index, a2, b2 = [list(i) for i in zip(*sab)]

    if a2 == sorted(a) and b2 == sorted(b):
        s = {i: index[i] for i in range(n)}

        l = [i for i in range(n)]
        ans = []
        pos = 0
        j = l[0]
        del l[0]
        for i in range(n):
            if pos != s[j]:
                ans.append([j, s[j]])
                if j in l:
                    l.remove(j)
                j = s[j]
            else:
                if j in l:
                    l.remove(j)
                if l:
                    pos = l[0]
                    j = l[0]
                    del l[0]
                else:
                    break

        print(len(ans))
        if ans:
            for i in ans:
                print(i[0]+1, i[1]+1)

    else:
        print(-1)
