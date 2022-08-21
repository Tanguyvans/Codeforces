for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    seq = [[0, float('inf')] for i in range(n)]
    seq[0][1] = a[0]

    for i in range(n):
        if seq[i][0] == 0:
            start = i+1
        else:
            start = i+2
        for j in range(start, min(i+4, n)):
            old = seq[j][1]
            seq[j][1] = min(seq[j][1], a[j]+seq[i][1])

            if old != seq[j][1] and j == start:
                seq[j][0] = 1

    print(min(seq[-1][1], seq[-2][1], seq[-3][1]))
