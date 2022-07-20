from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = Counter(a)
    ans = 0
    for k, v in b.items():
        ans += v-1

    if ans % 2 == 0:
        print(n-ans)
    else:
        print(n-ans-1)
