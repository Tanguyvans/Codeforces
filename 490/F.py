from collections import Counter


def func(pl, cd):
    if (pl, cd) in cmb:
        return cmb[(pl, cd)]
    elif pl == 1:
        if cd == 0:
            cmb[(pl, cd)] = 0
            return cmb[(pl, cd)]
        else:
            cmb[(pl, cd)] = h[min(k-1, cd-1)]
            return cmb[(pl, cd)]
    elif pl * k <= cd:
        cmb[(pl, cd)] = h[-1]*pl
        return cmb[(pl, cd)]
    else:
        sol = 0
        for i in range(min(k, cd), -1, -1):
            if i == 0:
                sol = max(sol, func(pl-1, max(0, cd-i)))
            else:
                inter = h[i-1] + func(pl-1, max(0, cd-i))
                sol = max(sol, inter)

        cmb[(pl, cd)] = sol
        return cmb[(pl, cd)]


n, k = list(map(int, input().split()))
c = list(map(int, input().split()))
f = list(map(int, input().split()))
h = list(map(int, input().split()))

p = {}
for i in range(n):
    if f[i] not in p:
        p[f[i]] = [1, 0]
    else:
        p[f[i]][0] += 1

for i in range(n*k):
    if c[i] in p:
        p[c[i]][1] += 1

ans = 0
cmb = {}
for key, val in p.items():
    n_players = val[0]
    n_cards = val[1]

    sol = func(n_players, n_cards)
    ans += sol

print(ans)
