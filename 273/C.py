import math

r, g, b = map(int, input().split())
d = {'r': r, 'g': g, 'b': b}
ans = 0
for i in range(10):
    a = ['r', 'r', 'g', 'g', 'b', 'b']
    b = ['g', 'b', 'r', 'b', 'r', 'g']

    end = True
    for i in range(6):
        ai = d[a[i]]
        bi = d[b[i]]
        if ai >= bi > 0 and max(ai, bi) >= 2:
            sol = ai-bi
            ans += sol
            d[a[i]] -= 2*sol
            d[b[i]] -= sol
            if sol != 0:
                end = False

    if end:
        ans += min(d['r'], d['g'], d['b'])
        break

print(ans)
