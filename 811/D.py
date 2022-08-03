for _ in range(int(input())):
    t = input()

    n = int(input())

    seq = [input() for i in range(n)]

    sol = [[float('inf') for j in range(len(t)+1)] for i in range(n)]
    occ = [[[] for j in range(len(t)+1)] for i in range(n)]

    for i in range(n):
        sol[i][0] = 0

    for i in range(1, len(t)+1):
        for j in range(n):
            p = seq[j]
            if i >= len(p):
                for k in range(n):
                    if sol[k][i-len(p)] < float('inf'):
                        if t[i-len(p):i] == p:
                            for l in range(i-len(p), i):
                                if sol[k][i-len(p)] + 1 < sol[j][l+1]:
                                    sol[j][l+1] = sol[k][i-len(p)] + 1
                                    occ[j][l+1] = occ[k][i-len(p)][:]
                                    occ[j][l+1].append((j+1, i-len(p)+1))

    ans = float('inf')
    position = -1
    for i in range(n):
        if sol[i][-1] <= ans:
            ans = sol[i][-1]
            position = i

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
        for x, y in occ[position][-1]:
            print(x, y)
