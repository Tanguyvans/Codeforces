for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split()))

    g = {i+1: [] for i in range(n)}

    root = 0
    for i in range(n):
        if a[i] == i+1:
            root = i+1
        else:
            g[a[i]].append(i+1)

    stack = []
    stack.append([root, 0])
    j = 1
    sol = {0: [root]}
    while stack:
        pos, nb = stack.pop()
        for cnt, k in enumerate(g[pos]):
            if cnt == 0:
                sol[nb].append(k)
                stack.append([k, nb])
            else:
                sol[j] = [k]
                stack.append([k, j])
                j += 1

    print(j)
    for k, v in sol.items():
        print(len(v))
        print(*v)
    print('')
