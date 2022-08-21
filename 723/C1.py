n = int(input())

a = list(map(int, input().split()))

matrix = [[-1 for i in range(n)] for j in range(n)]
matrix[0][0] = max(a[0], -1)
for i in range(1, n):
    if matrix[i-1][i-1] != -1:
        matrix[i][i] = max(a[i] + matrix[i-1][i-1], -1)
    matrix[0][i] = max(matrix[0][i-1], a[i])

ans = 0

for i in range(1, n):
    for j in range(i+1, n):
        sol = matrix[i][j-1]
        if matrix[i-1][j-1] >= 0:
            sol = max(sol, matrix[i-1][j-1]+a[j])

        matrix[i][j] = sol

    if matrix[i][-1] < 0:
        break

    ans = i+1

if n == 1 and a[0] >= 0:
    print(1)
else:
    print(ans)
