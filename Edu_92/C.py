from collections import Counter

for _ in range(int(input())):
    a = list(input())

    seq = {}
    ans = -1
    l = len(a)

    seq[a[0]] = 1

    for i in range(len(a)):
        if a[i] not in seq:
            seq[a[i]] = 1
        else:
            seq[a[i]] += 1

        s = ''.join(a[i-1:i+1])

        if s not in seq:
            seq[s] = 2
        else:
            seq[s] += 2

        ans = max(ans, seq[a[i]], seq[s])

    print(Counter(a))
    print(len(a))
