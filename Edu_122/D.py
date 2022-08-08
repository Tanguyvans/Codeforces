t = 1000
time = [t+1] * (t+1)
time[1] = 0
for i in range(1, t+1):
    for j in range(1, i+1):
        ni = i + i // j
        if ni <= t:
            time[ni] = min(time[ni], time[i]+1)


for _ in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    k = min(k, 12*n)
    for i in range(n):
        b[i] = time[b[i]]

    matrix = [[0 for j in range(k+1)] for i in range(n)]

    for i in range(n):
        for j in range(k+1):
            if j < b[i]:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(c[i] + matrix[i-1][j-b[i]], matrix[i-1][j])

    print(matrix[-1][-1])
