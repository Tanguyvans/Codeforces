from collections import Counter

for _ in range(int(input())):
    n = int(input())
    d = Counter()
    for i in map(int, input().split()):
        d[i] += 1

    d = sorted((d[i] for i in d), reverse=True)
    ans = 0
    seil = 10 ** 9
    for v in d:
        if v < seil:
            ans += v
            seil = v
        else:
            seil -= 1
            if seil == 0:
                break
            ans += seil

    print(ans)
