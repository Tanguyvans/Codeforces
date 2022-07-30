
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    seq = [1 for i in range(n)]
    seq[0] = 1
    ans = 1
    for i in range(n):
        for j in range(i, n, i+1):
            if j == i:
                continue
            if (j+1) % (i+1) == 0 and a[i] < a[j]:
                seq[j] = max(seq[j], seq[i]+1)
                ans = max(ans, seq[j])

    print(ans)
