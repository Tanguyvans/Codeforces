from collections import Counter
import math

for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split(' ')))

    b = [a[i]-i for i in range(n)]

    c = Counter(b)

    ans = 0
    for v in c.values():
        if v > 1:
            ans += int(v*(v-1)/2)

    print(ans)
