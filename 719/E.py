from collections import Counter

for _ in range(int(input())):

    n = int(input())

    a = input()
    a = [i for i in a]
    b = Counter(a)

    s = 0
    for k, v in b.items():
        if k == '*':
            s = v

    if s == 0:
        print(0)
    else:
        ans = 0
        f = False
        x = 0
        for i in range(n):
            if a[i] == '*':
                f = True
                x += 1

            if a[i] == '.' and f:
                ans += min(x, s-x)

        print(ans)
