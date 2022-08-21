def func(v, k, d, memo):
    if v in memo:
        return memo[v]
    else:
        memo[v] = [0, 0]
        nb = 0
        t = 0
        for i in range(1, k+1):
            if v-i > 0:
                ti, nbi = func(v-i, k, d, memo)
                if i >= d:
                    ti = nbi

            elif v-i == 0:
                if i >= d:
                    ti = 1
                    nbi = 1
                else:
                    ti = 0
                    nbi = 1

            else:
                break

            t += ti
            nb += nbi

        memo[v] = [t, nb]

        return memo[v]


n, k, d = map(int, input().split())

memo = {}
a, b = func(n, k, d, memo)

print(a % 1000000007)
