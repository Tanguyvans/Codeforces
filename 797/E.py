import math

for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))

    s = {i+1: 0 for i in range(k-1)}

    ans = 0
    for i in range(n):
        ans += math.floor(a[i]/k)
        if a[i] % k != 0:
            mod = a[i] % k
            if s[k-mod] != 0:
                s[k-mod] -= 1
                ans += 1
            else:
                s[mod] += 1

    for ki, v in s.items():
        if v != 0:
            for i in range(max(ki, k-ki), k):
                if s[i] > 0:
                    if i != ki:
                        val = min(v, s[i])
                        ans += val
                        s[i] -= val
                        v -= val
                    elif v >= 2:
                        ans += math.floor(v/2)
                        v = v % 2
    print(ans)
