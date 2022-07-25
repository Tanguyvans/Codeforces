n, m, k = map(int, input().split())

p = list(map(int, input().split()))

sol = [[0 for i in range(n)] for i in range(k+1)]

for i in range(1, k+1):
    s_1 = sum(p[(i-1)*m:m*i])
    s_t = sum(p[:i*m])
    for j in range(m-1+(i-1)*m, n):

        sol[i][j] = max(sol[i][j-1], sol[i-1][j-m] +
                        s_1, s_t)

        if j < n-1:
            s_1 = s_1 - p[j+1-m] + p[j+1]
            s_t = s_t - p[j+1-i*m] + p[j+1]

print(sol[-1][-1])
